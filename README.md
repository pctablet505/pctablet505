**I make ML models smaller and faster, then measure what each change bought.**

<a href="https://github.com/pctablet505/glm53-flash-single-gpu">
<picture>
  <source media="(max-width: 600px)" srcset="assets/glm53-decode-narrow.svg">
  <img src="assets/glm53-decode.svg" width="100%" alt="Decode speed in tokens per second: plain offloading 10.77, with a gather kernel 13.53, with a cache of the busiest experts 16.50 at peak, 14.99 as shipped. Router pruning reached 20.48 but was not shipped because it hurt the output.">
</picture>
</a>

| | |
|:--|:--|
| **10.8 → 15.0 tokens/s** | A 181 GiB LLM on one 96 GiB GPU, with my gather kernel and expert cache. [How →](https://github.com/pctablet505/glm53-flash-single-gpu) |
| **100 merged PRs** | In 38 open-source projects: Keras, KerasHub, vLLM, pip, pydantic. [See them →](https://github.com/search?q=is%3Apr+author%3Apctablet505+is%3Amerged+-user%3Apctablet505&type=pullrequests) |
| **3x faster** | On-device inference on a phone's NPU and DSP. |
| **70% → 90%** | Damaged-barcode accuracy, trained on 10M synthetic images. |

Also building [Porchlamp](https://porchlamp.org/) and [RL Alpha Labs](https://rlalphalabs.com/).

**Open to ML performance and on-device AI roles · [pctablet505.github.io](https://pctablet505.github.io/)**
