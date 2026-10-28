<a href="https://pctablet505.github.io/">
<img src="assets/banner-readme.png" width="100%" alt="Big models, small places, real numbers. pctablet505.">
</a>

I make models fit where they have to run, then check what they really do.

**What I work on**
- **LLM inference:** a 181 GiB model served from one 96 GiB GPU, decoding at 15.0 tokens a second, up from 10.8. [How](https://github.com/pctablet505/glm53-flash-single-gpu)
- **Computer vision:** face recognition at 30+ FPS on edge devices, with face search across 10,000+ people in 87 ms. A phone reads 90% of damaged barcodes, up from 70%.
- **On-device AI:** a drop detector with under 22 parameters does the work of a deep-learning model with millions, on over 95% less power. In Keras, one call exports a trained model for phones; I wrote [the keras.io guide](https://keras.io/guides/litert_export/).
- **Automated trading:** [RL Alpha Labs](https://rlalphalabs.com/) runs a survivorship-free NSE simulator and RL agents in JAX. An idea counts only if it beats an index fund after costs and tax.

**Open source:** [100 merged pull requests in 38 projects](https://github.com/search?q=is%3Apr+author%3Apctablet505+is%3Amerged+-user%3Apctablet505&type=pullrequests). 64 are in Keras and KerasHub, including [15 fixes for Keras on PyTorch](https://github.com/keras-team/keras/issues/22561#issuecomment-6247116051) and [Llama 3.1 in KerasHub](https://github.com/keras-team/keras-hub/pull/2132). The rest are spread across Python and ML tools people use every day: [pip](https://github.com/pypa/pip/pull/14179), [poetry](https://github.com/python-poetry/poetry/pull/10982), [pdm](https://github.com/pdm-project/pdm/pull/3815), [flit](https://github.com/pypa/flit/pull/806), [wheel](https://github.com/pypa/wheel/pull/694), [pydantic](https://github.com/pydantic/pydantic/pull/13452), [pyright](https://github.com/microsoft/pyright/pull/11547), [typeshed](https://github.com/python/typeshed/pull/16022), [trio](https://github.com/python-trio/trio/pull/3474), [vLLM](https://github.com/vllm-project/vllm/pull/56129), [skorch](https://github.com/skorch-dev/skorch/pull/1150) and pytest plugins ([randomly](https://github.com/pytest-dev/pytest-randomly/pull/735), [timeout](https://github.com/pytest-dev/pytest-timeout/pull/199), [rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures/pull/338)).

If you maintain a project, [Porchlamp](https://porchlamp.org/) shows how it treats a stranger's pull request, among 11,000 projects.
