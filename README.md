# Awesome-Computational-Pathology
<div align="center">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Computational Pathology](https://img.shields.io/badge/Topic-Computational%20Pathology-8A2BE2.svg)](#)
[![License](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE.txt)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**📜 A Curated List of Amazing Works in Computational Pathology, spanning whole-slide learning, pathology foundation models, multimodal pathology, spatial omics, vision-language models, and clinical applications.**  
*Focused on papers, benchmarks, datasets, and open-source repositories for modern computational pathology.*
<p align="center">
  <img src="assets/ACPATH.jpg" alt="Awesome World Models" width="100%" style="border-radius: 15px; box-shadow: 0 4px 24px rgba(0,0,0,.1); margin: 5px 0;">
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
- 🧠 [Definition of Computational Pathology](#definition-of-computational-pathology)
- 📖 [Surveys, Reviews, and Perspectives](#surveys-reviews-and-perspectives)
- 🗂️ [Datasets and Benchmarks](#datasets-and-benchmarks)
- 🧩 [Multiple Instance Learning](#multiple-instance-learning)
- 🤖 [Patch-Level Foundation Models](#patch-level-foundation-models)
- 🖼️ [Slide-Level Foundation Models and Slide Encoders](#slide-level-foundation-models-and-slide-encoders)
- 🧬 [Computational Pathology with Multi-Omics](#computational-pathology-with-multi-omics)
- 💬 [Vision-Language Models and Pathology Agents](#vision-language-models-and-pathology-agents)
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

## Definition of Computational Pathology

Computational pathology refers to the use of **algorithmic, statistical, and machine learning methods** to analyze digitized pathology data, especially whole-slide images (WSIs), region-of-interest (ROI) images, cell/nuclei annotations, reports, and paired molecular measurements.

Representative entry points include:

- **Computational Pathology: Challenges and Promises for Tissue Analysis**. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0462-y)

- **Computational Pathology: A Survey Review and The Way Forward**. [![arXiv](https://img.shields.io/badge/arXiv-2304.05482-b31b1b.svg)](https://arxiv.org/abs/2304.05482)

- **A Survey on Computational Pathology Foundation Models: Datasets, Adaptation Strategies, and Evaluation Tasks**. [![arXiv](https://img.shields.io/badge/arXiv-2501.15724-b31b1b.svg)](https://arxiv.org/abs/2501.15724)

- **A Survey of Pathology Foundation Models: Progress and Future Directions**. [![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-6A5ACD.svg)](https://www.ijcai.org/proceedings/2025/1193.pdf)

- **Pathology Feature Extractors and Foundation Models** — a living index of pathology encoders and FMs. [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)

---

## Surveys, Reviews, and Perspectives

### 1. General Computational Pathology
- **Computational Pathology: Challenges and Promises for Tissue Analysis**. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0462-y)

- **Computational Pathology: A Survey Review and The Way Forward**. [![arXiv](https://img.shields.io/badge/arXiv-2304.05482-b31b1b.svg)](https://arxiv.org/abs/2304.05482)

- **A Guide to Artificial Intelligence for Cancer Researchers**. [![Nature Reviews Cancer](https://img.shields.io/badge/Nature%20Reviews-Paper-8c564b.svg)](https://www.nature.com/articles/s41568-024-00757-5)

### 2. Foundation Models in Pathology
- **A Survey on Computational Pathology Foundation Models**. [![arXiv](https://img.shields.io/badge/arXiv-2501.15724-b31b1b.svg)](https://arxiv.org/abs/2501.15724)

- **A Survey of Pathology Foundation Models: Progress and Future Directions**. [![IJCAI 2025](https://img.shields.io/badge/IJCAI-2025-6A5ACD.svg)](https://www.ijcai.org/proceedings/2025/1193.pdf)

- **A Survey on Foundation and Vision-Language Models in Computational Pathology**. [![arXiv](https://img.shields.io/badge/arXiv-2408.14496-b31b1b.svg)](https://arxiv.org/abs/2408.14496)

- **Pathology Feature Extractors and Foundation Models**. [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)

### 3. Awesome Lists and Reading Lists
- **Awesome Digital and Computational Pathology**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/open-pathology/awesome-pathology)

- **Awesome Computational Pathology Papers**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/Awesome-Computational-Pathology-Papers)

- **Guide4PathAI**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/WonderLandxD/Guide4PathAI)

---

## Datasets and Benchmarks

### 1. Whole-Slide Classification and Grading
- **CAMELYON16** — lymph node metastasis detection benchmark. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON16-orange.svg)](https://camelyon16.grand-challenge.org/Data/)

- **CAMELYON17** — whole-slide and patient-level metastasis benchmark. [![Dataset](https://img.shields.io/badge/Dataset-CAMELYON17-orange.svg)](https://camelyon17.grand-challenge.org/)

- **PANDA** — large-scale prostate cancer grading benchmark. [![Dataset](https://img.shields.io/badge/Dataset-PANDA-orange.svg)](https://panda.grand-challenge.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/panda-challenge)

- **TCGA Processing Pipeline for MIL** — practical WSI preprocessing for weakly supervised learning. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/Pipeline-Processing-TCGA-Slides-for-MIL)

### 2. Nuclei / Cell-Level Datasets
- **PanNuke** — pan-cancer nuclei instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2003.10778) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/PanNuke-metrics)

- **NuCLS** — nucleus classification, localization, and segmentation dataset. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathologyDataScience/NuCLS)

### 3. Histology + Spatial Omics Benchmarks
- **HEST-1k / HEST-Benchmark** — histology + spatial transcriptomics benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)

- **HISTAI** — open-access whole-slide image resource for pathology AI. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.12120) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/HistAI/HISTAI)

- **MindLab-DP/Datasets** — practical collection of digital pathology datasets. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MindLab-DP/Datasets)

### 4. Unified Benchmarking Frameworks
- **UnPuzzle** — unified framework for pathology image analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.03152) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Puzzle-AI/UnPuzzle)

- **Patho-Bench** — standardized benchmark for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patho-Bench)

---

## Multiple Instance Learning

### 1. Foundational MIL Methods
- **ABMIL** — attention-based deep multiple instance learning. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/1802.04712) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AMLab-Amsterdam/AttentionDeepMIL)

- **CLAM** — clustering-constrained attention MIL for WSI classification. [![Nature Biomedical Engineering](https://img.shields.io/badge/Nature%20BME-Paper-1f77b4.svg)](https://www.nature.com/articles/s41551-020-00682-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)

- **DSMIL** — dual-stream MIL for WSI classification. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2011.08939) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/binli123/dsmil-wsi)

- **TransMIL** — correlated MIL with transformers. [![NeurIPS 2021](https://img.shields.io/badge/NeurIPS-2021-6A5ACD.svg)](https://proceedings.neurips.cc/paper/2021/hash/10c272d06794d3e5785d5e7c5356e9ff-Abstract.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/szc19990412/TransMIL)

- **HIPT** — hierarchical image pyramid transformer for gigapixel pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2206.02647) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HIPT)

### 2. Recent MIL Extensions and Reproducible Libraries
- **ACMIL** — attention-challenging MIL. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2311.07125) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/dazhangyu123/ACMIL)

- **MIL-Lab / FEATHER** — modern pathology MIL training library and pretrained aggregators. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/MIL-Lab)

- **PathBench-MIL** — benchmarking / AutoML framework for pathology MIL. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Sbrussee/PathBench-MIL)

- **MIL_BASELINE** — simple pathology MIL baseline template. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/MIL_BASELINE)

- **Awesome Multi-instance Learning for Whole Slide Images**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/peterlipan/Awesome-Multi-instance-Learning-for-Whole-Slide-Images)

---

## Patch-Level Foundation Models

### 1. Vision-Only Pathology Foundation Models
- **UNI** — general-purpose pathology foundation model. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02857-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/UNI)

- **Virchow** — million-slide digital pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2309.07778)

- **Virchow2** — large-scale pathology vision foundation model. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.00738) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Virchow2)

- **H-Optimus-1** — large histology encoder. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/bioptimus/H-optimus-1)

- **Hibou** — pathology vision transformers and downstream segmentation models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.05074) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histai/hibou)

- **PathoDuet** — foundation models for H&E and IHC slide analysis. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841524002147) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openmedlab/PathoDuet)

### 2. Vision-Language Pathology Foundation Models
- **CONCH** — contrastive learning from captions for histopathology. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)

- **MUSK** — multimodal transformer with unified masked modeling for precision oncology. [![Nature](https://img.shields.io/badge/Nature-Paper-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08437-2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)

---

## Slide-Level Foundation Models and Slide Encoders

### 1. Image-First Slide Encoders
- **Prov-GigaPath** — tile encoder + slide encoder for whole-slide representation learning. [![Nature](https://img.shields.io/badge/Nature-Paper-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07441-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/prov-gigapath/prov-gigapath)

- **CHIEF** — clinically oriented pathology foundation / slide encoder. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/CHIEF)

### 2. Multimodal Slide Foundation Models
- **TITAN** — multimodal whole-slide foundation model for pathology. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-025-03982-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TITAN)

- **CPath-Omni** — unified multimodal FM for patch and whole-slide analysis. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.12077) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)

---

## Computational Pathology with Multi-Omics

### 1. Histology + Spatial Transcriptomics
- **HEST-1k** — paired histology and spatial transcriptomics benchmark. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Dataset](https://img.shields.io/badge/Dataset-HuggingFace-orange.svg)](https://huggingface.co/datasets/MahmoodLab/hest) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)

- **Hist2ST** — gene expression prediction from histology images. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM-b31b1b.svg)](https://dl.acm.org/doi/10.1145/3503161.3548307) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/biomed-AI/Hist2ST)

- **THItoGene** — integrating histology and spatial transcriptomics for gene prediction. [![Paper](https://img.shields.io/badge/Paper-bioRxiv-b31b1b.svg)](https://www.biorxiv.org/content/10.1101/2024.01.25.577035v1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/yrjia1015/THItoGene)

- **BLEEP** — bimodal embedding for expression prediction. [![Paper](https://img.shields.io/badge/Paper-Nature%20Methods-b31b1b.svg)](https://www.nature.com/articles/s41592-024-02318-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bowang-lab/BLEEP)

- **MERGE** — hierarchical graph-based GNN for gene expression prediction from WSIs. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)

### 2. Histology + Spatial Proteomics / Cross-Stain Modeling
- **KRONOS** — foundation model for multiplex spatial proteomic images. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/KRONOS)

- **PathoDuet** — foundation models for H&E and IHC stains. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/abs/pii/S1361841524002147) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/openmedlab/PathoDuet)

- **SpatialFusion** — multimodal niche discovery from spatial transcriptomics + histology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uhlerlab/spatialfusion)

---

## Vision-Language Models and Pathology Agents

### 1. Patch- and Slide-Level Pathology VLMs
- **PathChat** — multimodal generative AI copilot for human pathology. [![Nature](https://img.shields.io/badge/Nature-Paper-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07618-3) [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.07814) [![Project](https://img.shields.io/badge/Project-AIHealth-blue.svg)](https://github.com/DeepReasoning/aihealth)

- **SlideChat** — large vision-language assistant for whole-slide pathology understanding. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.11761) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uni-medical/SlideChat)

- **CPath-Omni** — unified multimodal FM across patch and WSI scales. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.12077) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)

- **CONCH** — caption-aligned pathology VLM backbone. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)

- **MUSK** — precision oncology VLM. [![Nature](https://img.shields.io/badge/Nature-Paper-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08437-2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)

### 2. Related Benchmark / Tracking Resources
- **MLLM4BioMed** — tracking biomedical multimodal LLMs including pathology VLMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ncbi-nlp/MLLM4BioMed)

- **CVPR 2025 WSI Papers** — curated list of recent WSI and pathology VLM papers. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lingxitong/CVPR-2025-WSI-Papers)

---

## Clinical Tasks and Applications

### 1. Diagnosis and Whole-Slide Classification
- **CLAM** — weakly supervised cancer subtyping and WSI classification. [![Nature Biomedical Engineering](https://img.shields.io/badge/Nature%20BME-Paper-1f77b4.svg)](https://www.nature.com/articles/s41551-020-00682-w) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)

- **CHIEF** — pan-cancer slide representations for downstream clinical tasks. [![Nature Medicine](https://img.shields.io/badge/Nature%20Medicine-Paper-1f77b4.svg)](https://www.nature.com/articles/s41591-024-03141-0) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/CHIEF)

### 2. Nuclei / Tissue Segmentation and Cell Analysis
- **HoVer-Net** — simultaneous nuclear instance segmentation and classification. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)

- **CellViT** — ViT-based nuclei instance segmentation. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)

- **CellViT++ / Inference** — practical cell segmentation and WSI-scale inference stack. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT-plus-plus) [![Inference](https://img.shields.io/badge/Inference-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT-Inference)

### 3. Survival, Biomarkers, and Prognosis
- **VLSA** — interpretable vision-language survival analysis in pathology. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.04450) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/liupei101/VLSA)

- **LEAP** — pathology foundation model for urgent treatment prioritization and workflow support. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/hms-dbmi/LEAP)

### 4. Morphology-to-Molecular Prediction
- **Hist2ST** — spatial gene expression prediction from H&E. [![Paper](https://img.shields.io/badge/Paper-ACM%20MM-b31b1b.svg)](https://dl.acm.org/doi/10.1145/3503161.3548307) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/biomed-AI/Hist2ST)

- **MERGE** — graph-based morphology-to-expression modeling. [![Paper](https://img.shields.io/badge/Paper-CVPR%202025-b31b1b.svg)](https://arxiv.org/abs/2412.02601) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ags3927/MERGE)

---

## Evaluation, Metrics, and Reproducibility

### 1. Benchmark Libraries
- **Patho-Bench** — standardized evaluation for pathology foundation models. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/Patho-Bench)

- **HEST-Benchmark** — standardized morphology-to-expression benchmarking. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202024-b31b1b.svg)](https://arxiv.org/abs/2406.16192) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/HEST)

- **UnPuzzle** — unified pathology pipeline for controlled benchmarking. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.03152) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Puzzle-AI/UnPuzzle)

### 2. Robustness / Domain Shift
- **Histopath-C** — realistic corruption benchmark for histopathology VLMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Mehrdad-Noori/Histopath-C)

- **TRIDENT** — large-scale preprocessing + extraction toolkit that also supports reproducible WSI workflows. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)

---

## Interpretability, Explainability, and Trustworthiness

### 1. WSI / Feature Explainability
- **CLAM Heatmaps** — attention-based slide-level interpretability in weak supervision. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CLAM)

- **HistoXGAN** — explainability via histology reconstruction from latent features. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/fmhoward/HistoXGAN)

### 2. Cell- and Tissue-Level Interpretable Analysis
- **HoVer-Net** — interpretable nuclear detection / classification outputs. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841519301045) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vqdang/hover_net)

- **CellViT** — explicit cell instance outputs for pathology analysis. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TIO-IKIM/CellViT)

### 3. Trustworthiness / Quality Control
- **HistoQC** — whole-slide quality control for digital pathology cohorts. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/choosehappy/HistoQC)

- **GrandQC** — pathology quality control resource collected in awesome-pathology. [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://github.com/open-pathology/awesome-pathology)

---

## Resources, Toolkits, and Open-Source Projects

### 1. WSI Processing and IO
- **OpenSlide** — standard library for reading whole-slide images. [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://openslide.org/)

- **TRIDENT** — toolkit for large-scale WSI processing. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TRIDENT)

- **histolab** — Python library for digital pathology preprocessing. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histolab/histolab)

- **pathology-whole-slide-data** — WSI data pipelines and efficient batching. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/pathology-whole-slide-data)

- **AtlasPatch** — scalable tissue detection and patch extraction. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/AtlasAnalyticsLab/AtlasPatch)

### 2. End-to-End Pathology Toolkits
- **TIAToolbox** — end-to-end toolbox for computational pathology. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TissueImageAnalytics/tiatoolbox)

- **PathML** — pathology machine learning toolkit with pipelines and examples. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Dana-Farber-AIOS/pathml)

- **Slideflow** — whole-slide deep learning framework. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/slideflow/slideflow)

- **ASAP** — visualization, annotation, and automated slide analysis platform. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ComputationalPathologyGroup/ASAP)

### 3. Community Collections
- **Awesome Digital and Computational Pathology**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/open-pathology/awesome-pathology)

- **Awesome Computational Pathology Papers**. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DearCaat/Awesome-Computational-Pathology-Papers)

- **Pathology Feature Extractors and Foundation Models**. [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://github.com/georg-wolflein/pathology-foundation-models)

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
