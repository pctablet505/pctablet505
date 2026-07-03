# Hi, I'm Rahul 👋

**ML Engineer at Google, working on Keras** — I enjoy making machines a little
smarter every day, and making the smart ones run fast on small devices.
Previously at Qualcomm and Samsung R&D, building **face recognition, computer
vision, and sensor-driven systems** for millions of devices. Based in India 🇮🇳.

🌐 **[pctablet505.github.io](https://pctablet505.github.io)** · 💼 [LinkedIn](https://linkedin.com/in/rahul126) · 📈 1,000+ contributions in the last year

---

## ⚡ Open-source impact

**108 PRs authored** across Google's Keras ecosystem —
**43 merged** ([keras](https://github.com/keras-team/keras/pulls?q=is%3Apr+author%3Apctablet505+is%3Amerged) 26 ·
[keras-hub](https://github.com/keras-team/keras-hub/pulls?q=is%3Apr+author%3Apctablet505+is%3Amerged) 17) and
**35 in review** across keras, keras-hub, keras-io & litert-torch.

Merged work I'm proud of:

- [keras#22758](https://github.com/keras-team/keras/pull/22758) — **LiteRT export for the PyTorch backend**: on-device deployment of PyTorch-trained Keras 3 models
- [keras-hub#2132](https://github.com/keras-team/keras-hub/pull/2132) — **Llama 3.1 implemented in KerasHub**
- [keras#22362](https://github.com/keras-team/keras/pull/22362) — **serialization fix**: custom models with sublayers in nested lists failed to save/load
- [keras#22998](https://github.com/keras-team/keras/pull/22998) — **torch-backend `SymInt` handling** in `convert_to_tensor` and `slice`

In review right now: a **13-PR torch-performance series** (SDPA causal dispatch,
`convert_to_tensor` fast paths, …), **KerasHub → LiteRT-LM export**, and the
**official keras.io LiteRT export guide** —
[open PRs →](https://github.com/pulls?q=is%3Apr+author%3Apctablet505+is%3Aopen+org%3Akeras-team+org%3Agoogle-ai-edge)

---

## 🛠 What I work on

```mermaid
flowchart LR
    A["Frontier model<br/>(Gemma, …)"] --> B["Keras 3<br/>multi-backend"]
    B --> C["LiteRT / LiteRT-LM<br/>quantize + export"]
    C --> D["📱 On-device<br/>fast · private · offline"]
```

Edge & on-device AI · model optimization (quantization, latency, memory) ·
multi-backend Keras internals · computer vision & applied ML that actually ships.

Outside of Keras, my main project is **RL Alpha Labs** — a JAX-native
algorithmic-trading platform: PPO/DQN agents trading across **746 NSE
instruments** on 3.5+ years of market data, **128 vectorized environments**
for parallel rollout, and full portfolio simulation with risk controls.
The code is private, but there's a **[live demo →](https://pctablet505.github.io/RLAlphaLabs/)**

> 🕶 **The part you can't see here:** my major work before Google was
> **face recognition and face-related solutions** — plus computer-vision and
> camera/sensor problems — at Samsung R&D and Qualcomm. Real-time face auth
> serving 10,000+ registered faces on-device, embedding search cut from
> 1,200 ms → 87 ms, sensor-based drop detection at 95% less power. All
> closed-source, so GitHub only shows my Keras side.

---

## 🚀 Featured work

| Project | What it is |
|---|---|
| [RL Alpha Labs](https://pctablet505.github.io/RLAlphaLabs/) 🔒 | JAX-native RL trading platform — PPO/DQN over 746 NSE instruments, 128 vectorized envs, portfolio simulation with risk controls · private repo, [live demo](https://pctablet505.github.io/RLAlphaLabs/) |
| [ats-optimizer](https://github.com/pctablet505/ats-optimizer) | Truthful, human-in-the-loop job-application automation — feed-based discovery, knowledge vault, tailored resumes, ATS analysis |
| [litert-demo](https://github.com/pctablet505/litert-demo) | End-to-end export of KerasHub Gemma3 → LiteRT `.tflite` / LiteRT-LM `.litertlm` |
| [gemma-tflite-android-demo](https://github.com/pctablet505/gemma-tflite-android-demo) | Gemma running fully on-device on Android |
| [jax-windows-cuda-build](https://github.com/pctablet505/jax-windows-cuda-build) | CUDA build scripts, patches & pre-built JAX wheels for Windows |
| [daily_tracker](https://github.com/pctablet505/daily_tracker) | Cross-platform daily task tracker with Google Drive sync & auto-updates |
| [ML-Guide](https://github.com/pctablet505/ML-Guide) | Curated AI/ML learning path — courses, books, study notes |

---

## 📊 GitHub at a glance

<!-- Static self-generated cards (see gen_cards.py) — the shared
     github-readme-stats instance rate-limits and breaks randomly. -->
![GitHub activity](assets/stats-light.svg#gh-light-mode-only)![Top languages](assets/langs-light.svg#gh-light-mode-only)
![GitHub activity](assets/stats-dark.svg#gh-dark-mode-only)![Top languages](assets/langs-dark.svg#gh-dark-mode-only)

![GitHub Streak](https://streak-stats.demolab.com?user=pctablet505&theme=transparent)

---

## 📚 Currently exploring

- Better performance from smaller models — quantization, distillation, smarter kernels
- Synthetic data generation techniques
- Building a gallery search system
