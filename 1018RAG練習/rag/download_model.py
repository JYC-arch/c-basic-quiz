"""Download embedding weights only. No course material leaves this computer."""
import hashlib
import json
import os
import ssl
from pathlib import Path

os.environ['HF_HUB_DISABLE_XET'] = '1'
import httpx
from huggingface_hub import HfApi, hf_hub_download, set_client_factory

BASE = Path(__file__).resolve().parent
set_client_factory(lambda: httpx.Client(verify=ssl.create_default_context(), follow_redirects=True, timeout=120))
repo = 'Xenova/multilingual-e5-small'
target = BASE / 'model'
target.mkdir(exist_ok=True)
provenance = target / 'provenance.json'
revision = (json.loads(provenance.read_text('utf-8'))['revision']
            if provenance.exists() else HfApi().model_info(repo).sha)
files = ['config.json', 'tokenizer.json', 'tokenizer_config.json',
         'special_tokens_map.json', 'onnx/model_quantized.onnx']
hashes = {}
for filename in files:
    print('Downloading', filename, flush=True)
    path = Path(hf_hub_download(repo, filename, revision=revision, local_dir=target))
    hashes[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
(target / 'provenance.json').write_text(json.dumps({
    'repository': repo, 'revision': revision, 'files_sha256': hashes,
    'purpose': 'Local embedding encoder; not a retrieval content source'
}, indent=2), encoding='utf-8')
print('Model ready:', target, flush=True)
