<a href="https://pctablet505.github.io/">
<img src="assets/banner-readme.png" width="100%" alt="Big models, small places, real numbers. pctablet505.">
</a>

I make models fit where they have to run, then check what they really do.

**Upstream**
- **Keras on PyTorch:** 15 merged fixes, one root cause each. Compiled text generation on Keras master got 11.6x faster from July to October. [Progress report](https://github.com/keras-team/keras/issues/22561#issuecomment-6247116051)
- **LiteRT export in Keras and KerasHub:** one call turns a trained model into a file a phone runs. I wrote [the keras.io guide](https://keras.io/guides/litert_export/).
- **KerasHub:** added Llama 3.1, and fixed Gemma 3 bugs, including a preprocessor crash across Gemma 3, 3n and 4.
- **100 merged pull requests in 38 projects**, among them Keras, KerasHub, vLLM, pip and pydantic. [All of them](https://github.com/search?q=is%3Apr+author%3Apctablet505+is%3Amerged+-user%3Apctablet505&type=pullrequests)

**On phones**
- A drop detector with under 22 parameters, in place of a deep-learning model with millions: over 95% less power, accuracy 97% → 95.2%.
- Face recognition at 30+ FPS on edge devices, with face search across 10,000+ people in 87 ms.

**What I build** (pinned below)
- [A 181 GiB model on one 96 GiB GPU](https://github.com/pctablet505/glm53-flash-single-gpu): decoding from 10.8 to 15.0 tokens a second.
- [Porchlamp](https://porchlamp.org/): how 11,000 open-source projects treat a stranger's pull request. See where yours stands.
- [RL Alpha Labs](https://rlalphalabs.com/): automated trading on Indian stocks, on paper, judged against an index fund after costs and tax.
