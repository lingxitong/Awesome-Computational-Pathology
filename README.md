# Awesome-Computational-Pathology
<div align="center">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Computational Pathology](https://img.shields.io/badge/Topic-Computational%20Pathology-8A2BE2.svg)](#)
[![License](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE.txt)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**📜 A Curated List of Awesome Works in Computational Pathology, Aiming to Serve as a One-stop Resource for Researchers, Practitioners, and Enthusiasts Interested in Computational Pathology.**  
*Focused on papers, benchmarks, datasets, and open-source repositories for modern computational pathology.*
<p align="center">
  <img src="assets/ACPATH-logo.png" alt="Awesome World Models" width="100%" style="border-radius: 15px; box-shadow: 0 4px 24px rgba(0,0,0,.1); margin: 5px 0;">
</p>

*Photo Credit: [Gemini-Nano-Banana🍌](https://aistudio.google.com/models/gemini-2-5-flash-image)*.
</div>

---

## 🚩 News & Updates
_Major updates and repository announcements are shown below._

🚧 **[Ongoing] Repository Refocus** — This list is being rebuilt around **computational pathology**, with the original awesome-list visual style preserved.

🗂️ **[Ongoing] Curated by Topic** — Papers are organized by **datasets, MIL, patch-level FMs, slide-level FMs, multi-omics, pathology VLMs, and clinical applications**.

💡 **[Ongoing] Contributions Welcome** — If you would like to add missing papers, repos, or benchmarks, feel free to open a PR.

📌 **[Ongoing] Repository Support** — If this list helps your research, consider sharing the repository and citing it in your own awesome lists.

---

## Overview

- 🎯 [Aim of the Project](#aim-of-the-project)
- 📖 [Surveys, Reviews, and Perspectives](#surveys-reviews-and-perspectives)
- 🗂️ [Datasets and Benchmarks](#datasets-and-benchmarks)
- 🧩 [Multiple Instance Learning](#multiple-instance-learning)
- 🤖 [Patch-Level Foundation Models](#patch-level-foundation-models)
- 🖼️ [Slide-Level Foundation Models and Slide Encoders](#slide-level-foundation-models-and-slide-encoders)
- 🎨 [Generative Models for Computational Pathology](#generative-models-for-computational-pathology)
- 🧬 [Computational Pathology with Multi-Omics](#computational-pathology-with-multi-omics)
- 💬 [Vision-Language Models and Pathology Agents](#vision-language-models-and-pathology-agents)
- 🧱 [Dense Prediction in Computational Pathology](#dense-prediction-in-computational-pathology)
- 🏥 [Clinical Tasks and Applications](#clinical-tasks-and-applications)
- 📊 [Evaluation, Metrics, and Reproducibility](#evaluation-metrics-and-reproducibility)
- 🔬 [Interpretability, Explainability, and Trustworthiness](#interpretability-explainability-and-trustworthiness)
- 🚀 [Resources, Toolkits, and Open-Source Projects](#resources-toolkits-and-open-source-projects)
- 🙏 [Acknowledgements](#acknowledgements)
- 📝 [Citation](#citation)

---

## Aim of the Project

Computational pathology has rapidly evolved from handcrafted image analysis pipelines to **whole-slide learning**, **foundation models**, **multimodal pathology-language systems**, and **morphology-to-omics prediction**.  
At the same time, the literature has become fragmented across pathology, machine learning, computer vision, spatial biology, and multimodal AI.

This repository aims to:

- 🔍 **Organize** representative papers, datasets, toolkits, and repositories in computational pathology
- 🗺️ **Provide** a clean map of the field from classical WSI learning to modern foundation models
- 🤝 **Bridge** communities working on digital pathology, multimodal medicine, spatial biology, and medical AI
- 📚 **Serve** as a compact reading list for new researchers and a practical reference for experienced practitioners
- 🚀 **Track** open-source progress in pathology AI, especially around benchmarks and reproducibility

---

## Surveys, Reviews, and Perspectives

- **Computational Pathology: Challenges and Promises for Tissue Analysis**. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0462-y)
- **Computational Pathology: A Survey Review and The Way Forward**. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2304.05482)
- **A Guide to Artificial Intelligence for Cancer Researchers**. [![Paper](https://img.shields.io/badge/Paper-Nature%20Reviews%20Cancer-8c564b.svg)](https://www.nature.com/articles/s41568-024-00757-5)
- **A Survey on Computational Pathology Foundation Models**. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.15724)
- **A Survey of Pathology Foundation Models: Progress and Future Directions**. [![Paper](https://img.shields.io/badge/Paper-IJCAI%202025-6A5ACD.svg)](https://www.ijcai.org/proceedings/2025/1193.pdf)
- **A Survey on Foundation and Vision-Language Models in Computational Pathology**. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.14496)
- **Content Generation Models in Computational Pathology: A Comprehensive Survey on Methods, Applications, and Challenges**. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.21055) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yuanzhang7/Awesome-Generative-Models-in-Pathology)
- **Pathology Feature Extractors and Foundation Models**. [![Website](https://img.shields.io/badge/Website-GitHub-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)
- **Awesome Digital and Computational Pathology**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/open-pathology/awesome-pathology)
- **Awesome Computational Pathology Papers**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/Awesome-Computational-Pathology-Papers)
- **Guide4PathAI**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/WonderLandxD/Guide4PathAI)
- **Awesome Multi-instance Learning for Whole-Slide Images**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/peterlipan/Awesome-Multi-instance-Learning-for-Whole-Slide-Images)

---

## Datasets and Benchmarks

- **TCGA** — the most widely used public source for multi-cancer WSIs and linked clinical/molecular data. [![Dataset](https://img.shields.io/badge/Dataset-GDC-orange.svg)](https://portal.gdc.cancer.gov/)
- **CPTAC** — proteogenomic cohorts with matched histology and omics data. [![Dataset](https://img.shields.io/badge/Dataset-CPTAC-orange.svg)](https://proteomics.cancer.gov/programs/cptac)
- **CAMELYON16** — lymph node metastasis detection benchmark. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON16-orange.svg)](https://camelyon16.grand-challenge.org/Data/)
- **CAMELYON17** — whole-slide and patient-level metastasis benchmark. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON17-orange.svg)](https://camelyon17.grand-challenge.org/)
- **PANDA** — large-scale prostate cancer grading benchmark. [![Dataset](https://img.shields.io/badge/Dataset-PANDA-orange.svg)](https://panda.grand-challenge.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/panda-challenge)
- **PatchCamelyon (PCam)** — patch-level metastasis classification derived from CAMELYON. [![Dataset](https://img.shields.io/badge/Dataset-PCam-orange.svg)](https://github.com/basveeling/pcam)
- **MHIST** — minimalist colorectal polyp classification dataset. [![Dataset](https://img.shields.io/badge/Dataset-MHIST-orange.svg)](https://bmirds.github.io/MHIST/)
- **BRACS** — breast carcinoma subtyping benchmark with WSIs and ROIs. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data-b31b1b.svg)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575967/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histocartography/hact-net)
- **PanNuke** — pan-cancer nuclei instance segmentation and classification dataset. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2003.10778) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/PanNuke-metrics)
- **NuCLS** — nucleus classification, localization, and segmentation dataset. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathologyDataScience/NuCLS)
- **CoNSeP** — colorectal nuclear segmentation and phenotype dataset used heavily in nuclei benchmarks. [![Dataset](https://img.shields.io/badge/Dataset-CoNSeP-orange.svg)](https://warwick.ac.uk/fac/cross_fac/tia/data/hovernet/)
- **Lizard** — large-scale colonic nuclear instance segmentation and classification benchmark. [![Paper](https://img.shields.io/badge/Paper-ICCV%202021-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Graham_Lizard_A_Large-Scale_Dataset_for_Colonic_Nuclear_Instance_Segmentation_and_Classification_ICCV_2021_paper.html)
- **HEST-1k / HEST-Benchmark** — histology + spatial transcriptomics benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)
- **PathMMU** — expert-level benchmark for pathology large multimodal models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.16355) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathMMU-Benchmark/PathMMU) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathMMU)
- **PathBench** — multi-task, multi-organ benchmark for pathology foundation models. [![Website](https://img.shields.io/badge/Website-Leaderboard-blue.svg)](https://birkhoffkiki.github.io/PathBench/)
- **Patho-Bench** — standardized benchmark for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patho-Bench)
- **HISTAI** — open-access whole-slide pathology resource with expert annotations and models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.12120) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HistAI/HISTAI)
- **MindLab-DP/Datasets** — practical collection of digital pathology datasets. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MindLab-DP/Datasets)
- **TCGA Processing Pipeline for MIL** — practical WSI preprocessing pipeline for weak supervision. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/Pipeline-Processing-TCGA-Slides-for-MIL)

---

## Multiple Instance Learning

- **ABMIL** — attention-based deep multiple instance learning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/1802.04712) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AMLab-Amsterdam/AttentionDeepMIL)
- **CLAM** — clustering-constrained attention MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-Nature%20BME-1f77b4.svg)](https://www.nature.com/articles/s41551-020-00682-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)
- **DSMIL** — dual-stream MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2011.08939) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/binli123/dsmil-wsi)
- **TransMIL** — correlated MIL with transformers. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202021-6A5ACD.svg)](https://proceedings.neurips.cc/paper/2021/hash/10c272d06794d3e5785d5e7c5356e9ff-Abstract.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/szc19990412/TransMIL)
- **HIPT** — hierarchical transformer for gigapixel pathology with slide-level aggregation. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2206.02647) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HIPT)
- **DTFD-MIL** — double-tier feature distillation MIL. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_DTFD-MIL_Double-Tier_Feature_Distillation_Multiple_Instance_Learning_for_Histopathology_Whole_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hrzhang1123/DTFD-MIL)
- **Patch-GCN** — graph-based context-aware WSI survival modeling. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-b31b1b.svg)](https://arxiv.org/abs/2107.13048) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patch-GCN)
- **DT-MIL** — deformable transformer for MIL on histopathology. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-b31b1b.svg)](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_34) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yfzon/DT-MIL)
- **SparseConvMIL** — sparse convolutional context-aware MIL. [![Paper](https://img.shields.io/badge/Paper-MIDL%202021-b31b1b.svg)](https://proceedings.mlr.press/v156/lerousseau21a.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MarvinLer/SparseConvMIL)
- **HMIL** — hierarchical MIL for fine-grained WSI classification. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.07660) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ChengJin-git/HMIL)
- **MHIM-MIL** — masked hard instance mining for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-b31b1b.svg)](https://arxiv.org/abs/2307.10324) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/MHIM-MIL)
- **ILRA-MIL** — low-rank MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICLR%202023-6A5ACD.svg)](https://openreview.net/forum?id=8hH4Q3f8c2) [![Code](https://img.shields.io/badge/Code-MIL__BASELINE-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **WiKG** — whole-slide image as a knowledge graph. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://arxiv.org/abs/2403.07719) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/WonderLandxD/WiKG)
- **CA-MIL** — context-aware MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-ICLR%202024-6A5ACD.svg)](https://openreview.net/forum?id=rzBskAEmoc) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/olgarithmics/ICLR_CAMIL)
- **AC-MIL / ACMIL** — attention-challenging MIL. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-b31b1b.svg)](https://arxiv.org/abs/2403.05351) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dazhangyu123/ACMIL)
- **LongMIL** — long-contextual MIL for WSI analysis. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-6A5ACD.svg)](https://arxiv.org/abs/2410.14195) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/invoker-LL/Long-MIL)
- **RRT-MIL** — feature re-embedding toward foundation model-level performance. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Feature_Re-Embedding_Towards_Foundation_Model-Level_Performance_in_Computational_Pathology_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/RRT-MIL)
- **RetMIL** — retentive MIL for long histopathology sequences. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-b31b1b.svg)](https://papers.miccai.org/miccai-2024/657-Paper1723.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Hongbo-Chu/RetMIL)
- **MambaMIL** — Mamba-based long sequence MIL for computational pathology. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-b31b1b.svg)](https://arxiv.org/abs/2403.06800) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/isyangshu/MambaMIL)
- **cDP-MIL** — robust MIL via cascaded Dirichlet process. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-b31b1b.svg)](https://arxiv.org/abs/2407.11448) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HKU-MedAI/cDPMIL)
- **Lin-MIL** — linear attention MIL for scalable WSI analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.13417) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/charlotterchtr/Lin-MIL)
- **PackMIL** — pack-based MIL training framework for pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.12917) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/FangHeng/PackMIL)
- **MIL_BASELINE** — unified implementation hub for many pathology MIL methods. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **MIL-Lab / FEATHER** — standardized MIL library with pretrained slide models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)
- **MIL Tutorial** — hands-on tutorial for pathology MIL pipelines. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/guillaumejaume/mil-tutorial)

---

## Patch-Level Foundation Models

- **CTransPath** — transformer-based self-supervised pathology encoder. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841522002043) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Xiyue-Wang/TransPath)
- **PLIP** — pathology language-image pretraining. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-023-02504-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathologyFoundation/plip)
- **CONCH** — contrastive learning from captions for histopathology. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)
- **UNI** — general-purpose pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02857-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/UNI)
- **Virchow** — clinical-grade pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Virchow)
- **Phikon** — self-supervised histopathology ViT trained at scale. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-6A5ACD.svg)](https://arxiv.org/abs/2309.16864) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/HistoSSLscaling)
- **Phikon-v2** — upgraded Owkin pathology foundation model for weak supervision. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/owkin/phikon-v2)
- **H-Optimus-0** — large open histology foundation model. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/bioptimus/H-optimus-0)
- **H-Optimus-1** — next-generation H&E embedding model from Bioptimus. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/bioptimus/H-optimus-1)
- **Hibou** — DINOv2-based pathology vision transformers. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.05074) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histai/hibou)
- **Midnight** — competitive pathology FMs trained with far fewer WSIs. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-b31b1b.svg)](https://arxiv.org/abs/2504.05186) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/kaiko-ai/midnight)
- **OpenMidnight** — fully open replication and extension of Midnight. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MedARC-AI/OpenMidnight)
- **GPFM** — pathology foundation model implementation with downstream support. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/birkhoffkiki/GPFM)
- **MUSK** — multimodal transformer with unified masked modeling for pathology. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08437-2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)
- **Pathology Feature Extractors and Foundation Models** — ongoing community-maintained list of patch encoders and model cards. [![Website](https://img.shields.io/badge/Website-GitHub-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)

---

## Slide-Level Foundation Models and Slide Encoders

- **Prov-GigaPath** — whole-slide foundation model trained on real-world pathology data. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07441-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/prov-gigapath/prov-gigapath)
- **CHIEF** — clinical histopathology imaging evaluation foundation. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/CHIEF)
- **TITAN** — multimodal whole-slide foundation model for pathology. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-025-03982-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TITAN)
- **PANTHER** — morphological prototyping for unsupervised slide representation learning. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://arxiv.org/abs/2405.11643) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PANTHER)
- **TANGLE** — transcriptomics-guided slide representation learning. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://arxiv.org/abs/2405.11618) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TANGLE)
- **PRISM** — multimodal generative foundation model for slide-level histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.10254) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Prism)
- **THREADS** — molecular-driven foundation model for oncologic pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.16652)
- **FEATHER / MIL-Lab** — lightweight supervised slide foundation models. [![Paper](https://img.shields.io/badge/Paper-ICML%202025-6A5ACD.svg)](https://arxiv.org/abs/2506.09960) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)
- **Democratizing_WSI / GigaSSL** — optimized slide-level representations for TCGA-scale analysis. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/trislaz/Democratizing_WSI)
- **CPath-Omni** — unified multimodal foundation model spanning patches and WSIs. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.12077) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)
- **SlideChat** — large vision-language assistant with slide-level reasoning capability. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.11761) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uni-medical/SlideChat)
- **TRIDENT Slide Features** — practical extraction stack for multiple slide FMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)

---

## Computational Pathology with Multi-Omics

- **HEST-1k** — paired histology and spatial transcriptomics benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)
- **Hist2ST** — gene expression prediction from histology images. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM-b31b1b.svg)](https://dl.acm.org/doi/10.1145/3503161.3548307) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/biomed-AI/Hist2ST)
- **THItoGene** — histology to spatial transcriptomics prediction. [![Paper](https://img.shields.io/badge/Paper-bioRxiv-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.01.25.577035v1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yrjia1015/THItoGene)
- **BLEEP** — bimodal embedding model for morphology-to-expression prediction. [![Paper](https://img.shields.io/badge/Paper-Nature%20Methods-b31b1b.svg)](https://www.nature.com/articles/s41592-024-02318-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bowang-lab/BLEEP)
- **MERGE** — graph-based morphology-to-expression learning. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)
- **MCAT** — multimodal co-attention transformer for survival prediction in gigapixel WSIs. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202021-b31b1b.svg)](https://link.springer.com/chapter/10.1007/978-3-030-87240-3_67) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/mcat)
- **PathomicFusion** — multimodal fusion of histology and genomics. [![Paper](https://img.shields.io/badge/Paper-Cell%20Reports%20Medicine-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2666379122003171) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PathomicFusion)
- **PathOmics** — pathology-and-genomics multimodal transformer for survival outcome prediction. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-b31b1b.svg)](https://conferences.miccai.org/2023/papers/485-Paper1847.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Cassie07/PathOmics)
- **MMP** — multimodal prototyping for cancer survival prediction. [![Paper](https://img.shields.io/badge/Paper-ICML%202024-6A5ACD.svg)](https://proceedings.mlr.press/v235/song24b.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MMP)
- **SurvPath** — dense multimodal interactions between biological pathways and histology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shao_Modeling_Dense_Multimodal_Interactions_Between_Biological_Pathways_and_Histology_for_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/SurvPath)
- **PS3** — pathology reports + histology + pathways for cancer survival prediction. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-b31b1b.svg)](https://iccv.thecvf.com/virtual/2025/poster/1823) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/manahilr/PS3)
- **KRONOS** — foundation model for multiplex spatial proteomic images. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/KRONOS)
- **PathoDuet** — H&E and IHC foundation models for stain pairing and cross-stain transfer. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841524002147) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openmedlab/PathoDuet)
- **SpatialFusion** — multimodal niche discovery from spatial transcriptomics and histology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uhlerlab/spatialfusion)

---

## Generative Models for Computational Pathology


---

## Vision-Language Models and Pathology Agents

<em>Representative vision-language models, multimodal large language models, whole-slide image assistants, pathology agents, and reasoning-oriented systems for computational pathology.</em>

- **PathVQA** — pathology visual question answering dataset and benchmark for medical VQA. [![Paper](https://img.shields.io/badge/Paper-CVPR%20Workshop%202020-b31b1b.svg)](https://arxiv.org/abs/2003.10286)
- **TraP-VQA** — transformer-based pathology visual question answering with interpretable vision-language reasoning. [![Paper](https://img.shields.io/badge/Paper-JBHI%202022-b31b1b.svg)](https://ieeexplore.ieee.org/document/9733299)
- **K-PathVQA** — knowledge-aware multimodal representation learning for pathology visual question answering. [![Paper](https://img.shields.io/badge/Paper-JBHI%202023-b31b1b.svg)](https://ieeexplore.ieee.org/document/10177791)
- **MI-Zero** — multiple-instance zero-shot transfer for gigapixel histopathology images. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Lu_Visual_Language_Pretrained_Multiple_Instance_Zero-Shot_Transfer_for_Histopathology_Images_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MI-Zero)
- **PLIP / OpenPath** — visual-language foundation model for pathology image analysis using medical Twitter. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-023-02504-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathologyFoundation/plip)
- **Quilt-1M / QuiltNet** — million-scale histopathology image-text dataset and CLIP-style model. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-6A5ACD.svg)](https://openreview.net/forum?id=OL2JQoO0kq) [![Website](https://img.shields.io/badge/Website-Project-blue.svg)](https://quilt1m.github.io/)
- **PathAsst / PathCLIP** — generative foundation AI assistant and pathology-specific CLIP model. [![Paper](https://img.shields.io/badge/Paper-AAAI%202024-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/28308) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamessyx/pathclip)
- **CONCH** — caption-aligned visual-language foundation model for computational pathology. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/CONCH)
- **CONCH v1.5** — upgraded CONCH vision-language pathology encoder based on a larger ViT backbone. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/conchv1_5)
- **CPLIP** — comprehensive pathology language-image pretraining for zero-shot histopathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Javed_CPLIP_Zero-Shot_Learning_for_Histopathology_with_Comprehensive_Vision-Language_Alignment_CVPR_2024_paper.html) [![Website](https://img.shields.io/badge/Website-Project-blue.svg)](https://cplip.github.io/)
- **Quilt-LLaVA** — visual instruction tuning from localized narratives in open-source histopathology videos. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Seyfioglu_Quilt-LLaVA_Visual_Instruction_Tuning_by_Extracting_Localized_Narratives_from_Open-Source_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/aldraus/quilt-llava) [![Website](https://img.shields.io/badge/Website-Project-blue.svg)](https://quilt-llava.github.io/)
- **Dr-LLaVA** — visual instruction tuning with symbolic clinical grounding for medical and pathology dialogue. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.19567) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AlaaLab/Dr-LLaVA)
- **PathChat** — multimodal generative AI copilot for human pathology. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07618-3) [![Website](https://img.shields.io/badge/Website-Demo-blue.svg)](https://www.modella.ai/pathchat)
- **PathAlign** — vision-language model for whole-slide images aligned with pathology reports. [![Paper](https://img.shields.io/badge/Paper-PMLR%202024-b31b1b.svg)](https://proceedings.mlr.press/v254/ahmed24a.html) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.19578)
- **PRISM** — multi-modal generative foundation model for slide-level histopathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2405.10254) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Prism)
- **ViLa-MIL** — dual-scale vision-language multiple instance learning for whole-slide image classification. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_ViLa-MIL_Dual-scale_Vision-Language_Multiple_Instance_Learning_for_Whole_Slide_Image_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiangbo-Shi/ViLa-MIL)
- **HistGen** — histopathology report generation via local-global feature encoding and cross-modal interaction. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-b31b1b.svg)](https://papers.miccai.org/miccai-2024/387-Paper0796.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dddavid4real/HistGen)
- **PathM3** — multimodal multi-task multiple instance learning for WSI classification and captioning. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202024-b31b1b.svg)](https://papers.miccai.org/miccai-2024/593-Paper3991.html)
- **WSI-VQA** — generative visual question answering for interpreting whole-slide images. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-b31b1b.svg)](https://arxiv.org/abs/2407.05603) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cpystan/WSI-VQA)
- **PathMMU** — expert-level benchmark for pathology large multimodal models. [![Paper](https://img.shields.io/badge/Paper-ECCV%202024-b31b1b.svg)](https://arxiv.org/abs/2401.16355) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathMMU)
- **TM-PATHVQA** — textless multilingual pathology VQA dataset with spoken questions. [![Paper](https://img.shields.io/badge/Paper-INTERSPEECH%202024-b31b1b.svg)](https://www.isca-archive.org/interspeech_2024/rajkhowa24_interspeech.html) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2407.11383)
- **CLOVER** — cost-effective instruction learning for conversational pathology vision-language analysis. [![Paper](https://img.shields.io/badge/Paper-Nature%20Computational%20Science-1f77b4.svg)](https://www.nature.com/articles/s43588-025-00818-5) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jlinekai/clover)
- **PA-LLaVA / Pathology-LLaVA** — large language-vision assistant for human pathology image understanding. [![Paper](https://img.shields.io/badge/Paper-Artificial%20Intelligence%20Review-1f77b4.svg)](https://link.springer.com/article/10.1007/s10462-025-11190-1) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/OpenFace-CQUPT/Pathology-LLaVA)
- **PathInsight** — instruction tuning of multimodal datasets and models for histopathology diagnosis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.07037) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2408.07037)
- **Path-RAG** — knowledge-guided key region retrieval for open-ended pathology visual question answering. [![Paper](https://img.shields.io/badge/Paper-ML4H%202024-b31b1b.svg)](https://arxiv.org/abs/2411.17073)
- **MUSK** — vision-language foundation model for precision oncology with unified masked modeling. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08378-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)
- **WSI-LLaVA** — multimodal large language model for whole-slide image understanding. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_WSI-LLaVA_A_Multimodal_Large_Language_Model_for_Whole_Slide_Image_ICCV_2025_paper.html) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.02141)
- **TITAN** — transformer-based pathology image and text alignment network for whole-slide representation learning. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-025-03982-3) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/TITAN)
- **mSTAR** — multimodal knowledge-enhanced whole-slide pathology foundation model with reports and RNA-seq. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-025-66220-x)
- **PathGen-1.6M** — large-scale pathology image-text dataset generated through multi-agent collaboration. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-6A5ACD.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/jamessyx/PathGen)
- **PathGen-CLIP** — CLIP-style pathology VLM trained on PathGen-generated image-text pairs. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-6A5ACD.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamessyx/PathGen-CLIP)
- **PathGen-LLaVA** — pathology instruction-tuned model built on PathGen-generated image-text data. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-6A5ACD.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamessyx/PathGen-LLaVA)
- **MLLM4PUE** — universal pathology embeddings through multimodal large language models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.07221) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2502.07221)
- **PathVG / RefPath** — pathology visual grounding benchmark and language-grounded region dataset. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-b31b1b.svg)](https://papers.miccai.org/miccai-2025/0678-Paper1180.html) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/fengluo/RefPath)
- **MR-PLIP** — multi-resolution pathology-language pretraining with text-guided visual representation. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Albastaki_Multi-Resolution_Pathology-Language_Pre-training_Model_with_Text-Guided_Visual_Representation_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/BasitAlawode/MR-PLIP)
- **CPath-Omni** — unified multimodal foundation model for patch and whole-slide image analysis. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_CPath-Omni_A_Unified_Multimodal_Foundation_Model_for_Patch_and_Whole_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)
- **SlideChat** — whole-slide pathology vision-language assistant. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uni-medical/SlideChat) [![Website](https://img.shields.io/badge/Website-Project-blue.svg)](https://uni-medical.github.io/SlideChat.github.io/)
- **PathBench** — benchmark for patch- and whole-slide-level pathology image understanding by large multimodal models. [![Paper](https://img.shields.io/badge/Paper-TMI%202025-b31b1b.svg)](https://pubmed.ncbi.nlm.nih.gov/40601458/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/superjamessyx/PathBench)
- **PathoPrompt** — cross-granular semantic alignment for medical pathology vision-language models. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-b31b1b.svg)](https://papers.miccai.org/miccai-2025/0677-Paper4278.html)
- **ALPaCA / Llama-slideQA** — adapting Llama for pathology context analysis and slide-level question answering. [![Paper](https://img.shields.io/badge/Paper-medRxiv-b31b1b.svg)](https://www.medrxiv.org/content/10.1101/2025.04.22.25326190v1) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/CNX-PathLLM/Llama-slideQA)
- **HistoGPT** — report generation from gigapixel dermatopathology whole-slide images. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60014-x) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/marr-peng-lab/histogpt)
- **VLSA** — interpretable vision-language survival analysis with ordinal inductive bias for computational pathology. [![Paper](https://img.shields.io/badge/Paper-ICLR%202025-6A5ACD.svg)](https://openreview.net/forum?id=trj2Jq8riA) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/VLSA)
- **PolyPath** — large multimodal model adapted for multi-slide pathology report generation. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.10536)
- **ChatEXAONEPath** — expert-level multimodal large language model for histopathology using whole-slide images. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.13023)
- **OpenPath Active Learning** — open-set active learning for pathology image classification via pretrained vision-language models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.15318)
- **VideoPath-LLaVA** — pathology diagnostic reasoning through video instruction tuning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.04192) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/trinhvg/VideoPath-LLaVA)
- **PathGenIC** — histopathology image report generation with multimodal in-context learning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.17645)
- **PathCoT** — chain-of-thought prompting for zero-shot pathology visual reasoning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.01029)
- **SmartPath-R1** — versatile pathology copilot with reasoning-enhanced multimodal large language model. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.17303)
- **TCP-LLaVA** — efficient whole-slide pathology VQA via token compression. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.14497)
- **PathChat+ / SlideSeek** — clinical-grade multimodal pathology copilot and multi-agent WSI diagnostic reasoning system. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.20964)
- **WSI-Agents** — collaborative multi-agent system for multi-modal whole-slide image analysis. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202025-b31b1b.svg)](https://papers.miccai.org/miccai-2025/1022-Paper0994.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/CVI-SZU/WSI-Agents)
- **CPathAgent** — agent-based foundation model mimicking pathologists' high-resolution diagnostic logic. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202025-b31b1b.svg)](https://arxiv.org/abs/2505.20510)
- **PathFinder** — multi-modal multi-agent system for diagnostic decision-making in histopathology. [![Paper](https://img.shields.io/badge/Paper-ICCV%202025-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2025/html/Ghezloo_PathFinder_A_Multi-Modal_Multi-Agent_System_for_Medical_Diagnostic_Decision-Making_Applied_ICCV_2025_paper.html)
- **Pathology-CoT / Pathologist-o3** — visual chain-of-thought agent learned from expert whole-slide diagnostic behavior. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.04587) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2510.04587)
- **PathAgent** — training-free LLM-based agentic reasoning framework for interpretable whole-slide pathology analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.17052) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/G14nTDo4/PathAgent)
- **GIANT** — navigating gigapixel pathology images with large multimodal models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.19652) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2511.19652)
- **PathReasoning** — multimodal reasoning agent for query-based ROI navigation on whole-slide images. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.21902)
- **PathFound** — agentic multimodal model for pathological diagnosis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.23545)
- **LoC-Path** — learning to compress for pathology multimodal large language models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.05391)
- **MPath** — multimodal pathology report generation from whole-slide images using visual-prefix prompting. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.11906)
- **Democratising Pathology Co-Pilots / ANTONI-α** — open pipeline and dataset for whole-slide vision-language modelling. [![Paper](https://img.shields.io/badge/Paper-MIDL%202026-b31b1b.svg)](https://openreview.net/forum?id=aGPowreqPi) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.17326)
- **Hepato-LLaVA** — expert MLLM with sparse topo-pack attention for hepatocellular pathology analysis on WSIs. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.19424) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2602.19424)
- **MLLM-HWSI** — pathology slide analysis with multimodal LLMs for holistic whole-slide understanding. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.23067)
- **PBSBench** — multi-level vision-language benchmark and framework for pathology slide understanding. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.17570)
- **QCAgent** — quality-controllable agentic framework for grounded pathology report generation. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.01647)
- **KEEP** — knowledge-enhanced pathology vision-language model for diagnosis and differential diagnosis. [![Paper](https://img.shields.io/badge/Paper-Cancer%20Cell-1f77b4.svg)](https://www.sciencedirect.com/science/article/pii/S1535610826000589)
- **Patho-AgenticRAG** — multimodal agentic retrieval-augmented generation for pathology VLMs via reinforcement learning. [![Paper](https://img.shields.io/badge/Paper-AAAI%202026-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/40239) [![Paper](https://img.shields.io/badge/Paper-HuggingFace-yellow.svg)](https://huggingface.co/papers/2508.02258)
- **Patho-R1** — multimodal reinforcement learning-based pathology expert reasoner. [![Paper](https://img.shields.io/badge/Paper-AAAI%202026-b31b1b.svg)](https://arxiv.org/abs/2505.11404) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Wenchuan-Zhang/Patho-R1)
- **PathVLM-R1** — reinforcement learning-driven reasoning model for pathology visual-language tasks. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.09258)
- **DiagR1** — vision-language model trained via reinforcement learning for digestive pathology diagnosis. [![Paper](https://img.shields.io/badge/Paper-JBHI-b31b1b.svg)](https://ieeexplore.ieee.org/document/11419719) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.18433)
- **PathoHR** — hierarchical reasoning for vision-language models in pathology. [![Paper](https://img.shields.io/badge/Paper-EMNLP%20Findings%202025-b31b1b.svg)](https://aclanthology.org/2025.findings-emnlp.124/)
- **PathReasoner-R1** — structured pathology reasoning via knowledge-guided policy optimization. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.21617) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cyclexfy/PathReasoner-R1)
- **PathVLM-Eval** — evaluation of open vision-language models for pathology image understanding. [![Paper](https://img.shields.io/badge/Paper-JPI%202025-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S2153353925000409)
- **DomainSAT for Pathology VLMs** — detecting performance degradation under data shift in pathology VLMs. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.00716)
- **MLLM4BioMed** — broad tracker for biomedical multimodal LLMs, including pathology VLMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ncbi-nlp/MLLM4BioMed)

---


## Dense Prediction in Computational Pathology


---

## Clinical Tasks and Applications

- **CLAM** — data-efficient weak supervision for tumor classification and subtyping. [![Paper](https://img.shields.io/badge/Paper-Nature%20BME-1f77b4.svg)](https://www.nature.com/articles/s41551-020-00682-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)
- **CHIEF** — pan-cancer slide representations for downstream clinical prediction. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/CHIEF)
- **HoVer-Net** — simultaneous nuclei instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)
- **CellViT** — transformer-based nuclei instance segmentation and classification. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)
- **CellViT++** — improved whole-slide cell segmentation stack. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT-plus-plus)
- **CellViT-Inference** — scalable inference pipeline for cell-level pathology analysis. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT-Inference)
- **DeepLIIF** — virtual multiplex immunofluorescence and IHC quantification. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/nadeemlab/DeepLIIF)
- **HistoSegNet** — histological tissue-type segmentation. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uzh-rpg/HistoSegNet)
- **StarDist** — star-convex object detection for nuclei and cells. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/stardist/stardist)
- **MSINet** — microsatellite instability prediction from histology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/KatherLab/STAMP)
- **LEAP** — pathology FM for urgent treatment prioritization and workflow support. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/LEAP)
- **VLSA** — interpretable vision-language survival analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.04450) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/VLSA)
- **Hist2ST** — morphology-to-expression prediction as a clinically relevant downstream task. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM-b31b1b.svg)](https://dl.acm.org/doi/10.1145/3503161.3548307) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/biomed-AI/Hist2ST)
- **MERGE** — graph-based molecular biomarker prediction from pathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)
- **EPIC-Survival** — end-to-end survival analysis with prognostic clustering. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MSKCC-Computational-Pathology/EPIC-Survival)
- **MRePath** — multimodal rebalanced pathology-genomics survival prediction. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MCPathology/MRePath)

---

## Evaluation, Metrics, and Reproducibility

- **Patho-Bench** — standardized evaluation for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patho-Bench)
- **PathBench** — live benchmark for pathology foundation models and clinical tasks. [![Website](https://img.shields.io/badge/Website-Leaderboard-blue.svg)](https://birkhoffkiki.github.io/PathBench/)
- **HEST-Benchmark** — morphology-to-expression evaluation benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)
- **PathMMU** — expert benchmark for pathology LMM evaluation. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.16355) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathMMU-Benchmark/PathMMU)
- **PathBench-MIL** — benchmarking and AutoML framework for pathology MIL. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/birkhoffkiki/PathBench-MIL)
- **PLISM Benchmark** — robustness benchmark for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/plism-benchmark)
- **Histopath-C** — realistic corruption benchmark for histopathology foundation/VL models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.12493) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Mehrdad-Noori/Histopath-C)
- **STAMP-Benchmark** — clinical benchmark of public self-supervised pathology FMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/KatherLab/STAMP-Benchmark)
- **MIL_BASELINE** — unified MIL implementations that improve method comparability. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **MIL-Lab** — standardized implementations and pretrained FEATHER models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)
- **UnPuzzle** — unified pathology image analysis pipeline for controlled benchmarking. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.03152) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Puzzle-AI/UnPuzzle)
- **TRIDENT** — reproducible large-scale WSI preprocessing and feature extraction. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)

---

## Interpretability, Explainability, and Trustworthiness

- **CLAM Heatmaps** — attention-based slide-level interpretability in weak supervision. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)
- **VLSA** — vision-language survival analysis with interpretable text-guided reasoning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.04450) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/VLSA)
- **HistoGPT** — report generation with word/phrase-to-region visualization. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60014-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/marrlab/HistoGPT)
- **HistoXGAN** — reconstructive explainability for histology representations. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/fmhoward/HistoXGAN)
- **HoVer-Net** — explicit nuclei instances and categories for cell-level interpretation. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)
- **CellViT** — interpretable cell-centric outputs for pathology analysis. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)
- **HistoQC** — whole-slide quality control and artifact detection. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/choosehappy/HistoQC)
- **GrandQC** — large-scale pathology quality control with TCGA masks and artifact maps. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-024-54769-y) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/cpath-ukk/grandqc)
- **FrOoDo** — framework for out-of-distribution artifact detection in pathology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MECLabTUDA/FrOoDo)
- **Histopath-C** — robustness and corruption stress test for pathology models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.12493) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Mehrdad-Noori/Histopath-C)

---

## Resources, Toolkits, and Open-Source Projects

- **OpenSlide** — standard library for reading whole-slide images. [![Website](https://img.shields.io/badge/Website-OpenSlide-blue.svg)](https://openslide.org/)
- **QuPath** — widely used open-source platform for digital pathology viewing and analysis. [![Website](https://img.shields.io/badge/Website-QuPath-blue.svg)](https://qupath.github.io/)
- **ASAP** — visualization, annotation, and automated slide analysis platform. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ComputationalPathologyGroup/ASAP)
- **caMicroscope** — digital pathology viewer with support for human and machine annotations. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/camicroscope/caMicroscope)
- **TRIDENT** — toolkit for large-scale WSI processing and feature extraction. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)
- **TIAToolbox** — end-to-end toolbox for computational pathology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/tiatoolbox)
- **PathML** — pathology ML toolkit with pipelines and examples. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Dana-Farber-AIOS/pathml)
- **Slideflow** — whole-slide deep learning framework for research and deployment. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/slideflow/slideflow)
- **histolab** — Python library for preprocessing digital pathology slides. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histolab/histolab)
- **pathology-whole-slide-data** — data pipelines and efficient WSI batch iterators. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/pathology-whole-slide-data)
- **AtlasPatch** — scalable tissue detection and patch extraction. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AtlasAnalyticsLab/AtlasPatch)
- **LazySlide** — modern pathology analysis utilities with model zoo support. [![Website](https://img.shields.io/badge/Website-Docs-blue.svg)](https://lazyslide.readthedocs.io/)
- **HistoQC** — practical quality control toolbox for large slide cohorts. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/choosehappy/HistoQC)
- **MIL_BASELINE** — unified pathology MIL library. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)
- **MIL-Lab** — standardized MIL codebase with FEATHER checkpoints. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)
- **PFM_Segmentation** — segmentation framework built around pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/PFM_Segmentation)
- **PrismToolBox** — toolbox for patch extraction, embeddings, and QuPath interoperability. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/gustaveroussy/prismtoolbox)
- **Awesome Digital and Computational Pathology**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/open-pathology/awesome-pathology)
- **Awesome Computational Pathology Papers**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/Awesome-Computational-Pathology-Papers)
- **Pathology Feature Extractors and Foundation Models**. [![Website](https://img.shields.io/badge/Website-GitHub-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)

---

## Acknowledgements

This list benefits from the open-source efforts of many groups across **computational pathology**, **spatial biology**, **medical vision-language modeling**, and **digital pathology infrastructure**.

Special thanks to the maintainers of:
- **Mahmood Lab**
- **PathFoundation / open-pathology**
- **Tissue Image Analytics**
- **DIAGNijmegen**
- **HistAI**
- **many community-maintained awesome lists and benchmark repositories**

---

## Citation

If you find this repository helpful, please consider citing it in your own project page or awesome list.

```bibtex
@misc{awesome_computational_pathology,
  title={Awesome Computational Pathology},
  author={Contributors},
  year={2026},
  howpublished={\url{https://github.com/your-repo/awesome-computational-pathology}}
}
```
