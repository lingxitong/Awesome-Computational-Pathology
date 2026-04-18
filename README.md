# Awesome-Computational-Pathology
<div align="center">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md) [![License](https://img.shields.io/badge/License-CC0_1.0-blue.svg)](LICENSE.txt)

**🔬 A Curated List of Awesome Works in Computational Pathology, Aiming to Serve as a One-stop Resource for Researchers, Practitioners, and Enthusiasts Interested in Computational Pathology..**

</div>

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

Computational pathology has rapidly evolved from handcrafted feature engineering and patch-based classification to whole-slide learning, pathology foundation models, multimodal vision-language systems, and clinically oriented pathology agents.

This repository aims to:

- 🔍 **Organize** representative papers and codebases across the major subareas of computational pathology.
- 🗺️ **Provide** a clean roadmap from classical WSI pipelines to recent pathology foundation models and multimodal systems.
- 🧱 **Bridge** patch-level modeling, slide-level representation learning, nuclei/cell analysis, pathology-language modeling, and omics integration.
- 📚 **Serve** as a practical starting point for students, researchers, and engineers entering the field.
- 🚀 **Track** open-source resources that are actually useful for reproduction, benchmarking, and downstream development.

This list is intentionally **curated rather than exhaustive**. The goal is not to collect every paper, but to keep the structure readable and useful.

---

## Definition of Computational Pathology

Computational pathology studies how to extract quantitative, reproducible, and clinically meaningful information from pathology images, especially whole-slide images (WSIs), using computer vision, machine learning, multimodal learning, and increasingly foundation models.

Typical research objects include:

- **Patch / ROI-level pathology images**
- **Whole-slide images (WSIs)**
- **Cell / nuclei morphology and spatial organization**
- **Pathology reports and pathology-language supervision**
- **Genomics, transcriptomics, and spatial omics paired with histology**

Typical downstream tasks include:

- Slide-level classification and subtyping
- Tumor detection and grading
- Biomarker and mutation prediction
- Survival / prognosis modeling
- Nuclei / cell / tissue segmentation
- Report generation and pathology VQA
- Histology-omics alignment and gene expression prediction

---

## Surveys, Reviews, and Perspectives

### Selected surveys

- **A Survey on Computational Pathology Foundation Models**  
  - **Summary:** A focused survey on pathology foundation models, including datasets, pretraining paradigms, adaptation strategies, and evaluation settings.  
  - **Paper:** https://arxiv.org/abs/2501.15724  
  - **Code / Project:** https://github.com/georg-wolflein/pathology-foundation-models

- **A Survey of Pathology Foundation Model: Progress and Perspectives**  
  - **Summary:** A more taxonomy-oriented survey discussing patch encoders, slide encoders, multimodal models, and future directions.  
  - **Paper:** https://www.ijcai.org/proceedings/2025/1193.pdf  
  - **Code / Project:** https://github.com/georg-wolflein/pathology-foundation-models

- **Pathology Feature Extractors and Foundation Models**  
  - **Summary:** A living list of pathology feature extractors and foundation models, useful as a practical companion resource.  
  - **Paper / Project:** https://github.com/georg-wolflein/pathology-foundation-models

- **Awesome Digital and Computational Pathology**  
  - **Summary:** A broad open-source collection spanning datasets, segmentation, WSI analysis, multimodal pathology, and tooling.  
  - **Project:** https://github.com/open-pathology/awesome-pathology

- **Awesome Computational Pathology Papers**  
  - **Summary:** A fast-moving collection of recent computational pathology papers, especially useful for tracking 2024–2025 model releases.  
  - **Project:** https://github.com/DearCaat/Awesome-Computational-Pathology-Papers

---

## Datasets and Benchmarks

### Whole-slide classification and grading

- **CAMELYON16 / CAMELYON17**  
  - **Type:** WSI metastasis detection benchmark  
  - **Summary:** A classic benchmark for lymph node metastasis detection and one of the most influential entry points into weakly supervised WSI learning.  
  - **Dataset:** https://camelyon16.grand-challenge.org/Data/  
  - **Related Code:** https://github.com/arjunvekariyagithub/camelyon16-grand-challenge

- **PANDA**  
  - **Type:** WSI prostate grading benchmark  
  - **Summary:** A large public WSI dataset for prostate cancer grading collected from Radboud University Medical Center and Karolinska Institute.  
  - **Dataset Intro:** https://github.com/DIAGNijmegen/panda-challenge/blob/main/notebooks/getting-started-with-the-panda-dataset.ipynb  
  - **Winning Solution:** https://github.com/kentaroy47/Kaggle-PANDA-1st-place-solution

- **TCGA Processing Pipeline for MIL**  
  - **Type:** WSI data processing and benchmarking support  
  - **Summary:** Not a dataset release by itself, but one of the most useful public pipelines for turning TCGA slides into reproducible MIL-ready data.  
  - **Project:** https://github.com/liupei101/Pipeline-Processing-TCGA-Slides-for-MIL

### Nuclei / cell-level datasets

- **PanNuke**  
  - **Type:** Pan-cancer nuclei instance segmentation and classification  
  - **Summary:** A widely used nuclei benchmark covering multiple tissue types and nuclei classes.  
  - **Paper:** https://arxiv.org/abs/2003.10778  
  - **Metrics / Evaluation:** https://github.com/TissueImageAnalytics/PanNuke-metrics

- **NuCLS**  
  - **Type:** Nucleus classification, localization, and segmentation  
  - **Summary:** A large breast pathology nuclei dataset with crowd-assisted and expert-refined labels.  
  - **Paper / Dataset:** https://github.com/PathologyDataScience/NuCLS

### Histology + spatial omics / multimodal benchmarks

- **HEST-1k / HEST-Benchmark**  
  - **Type:** Histology + spatial transcriptomics benchmark  
  - **Summary:** A major recent benchmark for evaluating pathology foundation models on morphology-to-expression transfer and multimodal learning.  
  - **Project:** https://github.com/mahmoodlab/HEST  
  - **Dataset Card:** https://huggingface.co/datasets/MahmoodLab/hest

- **HISTAI**  
  - **Type:** Large-scale open WSI dataset  
  - **Summary:** A large open-access WSI resource designed to improve openness, reproducibility, and downstream evaluation breadth in computational pathology.  
  - **Paper:** https://arxiv.org/abs/2505.12120  
  - **Project:** https://github.com/HistAI/HISTAI

- **UnPuzzle Benchmark**  
  - **Type:** Unified pathology benchmarking framework  
  - **Summary:** A framework for benchmarking both ROI and WSI models under a unified experimental pipeline.  
  - **Paper:** https://arxiv.org/abs/2503.03152  
  - **Code:** https://github.com/Puzzle-AI/UnPuzzle

---

## Multiple Instance Learning

Multiple Instance Learning (MIL) remains the dominant paradigm for weakly supervised WSI classification. A slide is treated as a bag of patch embeddings, and the main modeling question is how to aggregate instance evidence into a slide-level prediction.

### Foundational MIL methods

- **Attention-based Deep Multiple Instance Learning (ABMIL)**  
  - **Summary:** The classical attention-pooling MIL method that influenced much of modern WSI aggregation.  
  - **Paper:** https://arxiv.org/abs/1802.04712  
  - **Code:** https://github.com/AMLab-Amsterdam/AttentionDeepMIL

- **CLAM**  
  - **Summary:** One of the most influential WSI MIL frameworks, emphasizing data-efficient weak supervision and attention-based instance selection.  
  - **Paper:** https://www.nature.com/articles/s41551-020-00682-w  
  - **Code:** https://github.com/mahmoodlab/CLAM

- **DSMIL**  
  - **Summary:** A dual-stream MIL method that became a strong and widely reused baseline for slide classification.  
  - **Paper:** https://arxiv.org/abs/2011.08939  
  - **Code:** https://github.com/binli123/dsmil-wsi

- **TransMIL**  
  - **Summary:** A transformer-based correlated MIL framework that explicitly models inter-instance correlation beyond i.i.d. assumptions.  
  - **Paper:** https://proceedings.neurips.cc/paper/2021/hash/10c272d06794d3e5785d5e7c5356e9ff-Abstract.html  
  - **Code:** https://github.com/szc19990412/transmil

- **HIPT**  
  - **Summary:** A hierarchical transformer framework connecting patch- and region-scale representations for gigapixel pathology.  
  - **Paper:** https://arxiv.org/abs/2206.02647  
  - **Code:** https://github.com/mahmoodlab/HIPT

### Recent MIL extensions

- **ACMIL**  
  - **Summary:** A more recent attention-oriented MIL variant designed for stronger WSI classification under weak supervision.  
  - **Paper:** https://arxiv.org/abs/2311.07125  
  - **Code:** https://github.com/dazhangyu123/ACMIL

- **MIL-Lab / FEATHER**  
  - **Summary:** A modern open repository for MIL training and pretrained ABMIL-style aggregators on large pathology cohorts.  
  - **Project:** https://github.com/mahmoodlab/MIL-Lab

- **Awesome MIL for WSI**  
  - **Summary:** A curated companion list for researchers specifically interested in WSI MIL literature.  
  - **Project:** https://github.com/peterlipan/Awesome-Multi-instance-Learning-for-Whole-Slide-Images

---

## Patch-Level Foundation Models

Patch-level pathology foundation models learn transferable histology representations from large-scale image pretraining, usually via self-supervised learning or vision-language alignment.

- **UNI**  
  - **Type:** General-purpose pathology vision foundation model  
  - **Summary:** One of the most widely adopted open pathology encoders for downstream patch and WSI pipelines.  
  - **Paper:** https://www.nature.com/articles/s41591-024-02857-3  
  - **Code:** https://github.com/mahmoodlab/UNI

- **CONCH**  
  - **Type:** Vision-language pathology foundation model  
  - **Summary:** A pathology-specific visual-language foundation model trained with large-scale image-caption pairs, often used as a strong patch encoder.  
  - **Paper:** https://www.nature.com/articles/s41591-024-02856-4  
  - **Code:** https://github.com/mahmoodlab/CONCH

- **Virchow / Virchow2**  
  - **Type:** Large-scale pathology vision foundation models  
  - **Summary:** Paige’s Virchow family pushed scale, diversity, and mixed-magnification training for histopathology pretraining.  
  - **Paper (Virchow2):** https://arxiv.org/abs/2408.00738  
  - **Weights / Model Card:** https://huggingface.co/paige-ai/Virchow2

- **H-Optimus-1**  
  - **Type:** Large histology foundation model  
  - **Summary:** A very large pathology encoder released with an emphasis on high-fidelity embeddings for downstream pathology tasks.  
  - **Model Card:** https://huggingface.co/bioptimus/H-optimus-1  
  - **Fine-tuning Example:** https://github.com/aws-samples/ai-digital-pathology

- **Hibou**  
  - **Type:** DINOv2-style pathology vision transformers  
  - **Summary:** A family of pathology vision transformers trained at scale and used in both patch-level and downstream WSI pipelines.  
  - **Paper:** https://arxiv.org/abs/2406.05074  
  - **Code:** https://github.com/histai/hibou

---

## Slide-Level Foundation Models and Slide Encoders

Slide-level models move beyond independent patch encoding and aim to learn **whole-slide** or **patient-level** representation spaces directly.

- **Prov-GigaPath**  
  - **Type:** Image-first slide foundation model  
  - **Summary:** A landmark open-weight whole-slide model containing both a tile encoder and a slide encoder.  
  - **Paper:** https://www.nature.com/articles/s41586-024-07441-w  
  - **Code:** https://github.com/prov-gigapath/prov-gigapath

- **CHIEF**  
  - **Type:** Clinical-grade pathology foundation model / slide encoder  
  - **Summary:** A clinically oriented pathology foundation model emphasizing robustness across cancers and rare cancer detection.  
  - **Paper:** https://www.nature.com/articles/s41591-024-03141-0  
  - **Code:** https://github.com/hms-dbmi/CHIEF

- **TITAN**  
  - **Type:** Multimodal whole-slide foundation model  
  - **Summary:** A major recent whole-slide model combining visual SSL and pathology-language supervision for slide representation learning, retrieval, zero-shot use, and report generation.  
  - **Paper:** https://www.nature.com/articles/s41591-025-03982-3  
  - **Code:** https://github.com/mahmoodlab/TITAN

- **PRISM / PRISM2**  
  - **Type:** Multimodal slide-level foundation models  
  - **Summary:** A multimodal slide embedding framework using pathology images and clinical text for slide-level reasoning and report-style generation.  
  - **Model Card (PRISM):** https://huggingface.co/paige-ai/Prism  
  - **Paper (PRISM2):** https://arxiv.org/abs/2506.13063

- **Threads**  
  - **Type:** Molecularly driven slide foundation model  
  - **Summary:** A slide-level foundation model pretrained using paired histology, genomics, and transcriptomics.  
  - **Paper:** https://arxiv.org/abs/2501.16652

- **mSTAR**  
  - **Type:** Multimodal whole-slide pretraining framework  
  - **Summary:** A whole-slide pretraining strategy that injects multimodal context into pathology foundation model learning.  
  - **Paper:** https://arxiv.org/abs/2407.15362  
  - **Code:** https://github.com/Innse/mSTAR

---

## Computational Pathology with Multi-Omics

This line of work studies how histology can be aligned with transcriptomics, genomics, methylation, or spatial omics, either for representation learning or for direct molecular prediction.

- **HE2RNA**  
  - **Type:** Histology-to-transcriptomics prediction  
  - **Summary:** A pioneering method showing that transcriptomic profiles can be predicted from WSIs without dense expert annotation.  
  - **Paper:** https://www.nature.com/articles/s41467-020-17678-4  
  - **Code:** https://github.com/owkin/HE2RNA_code

- **TANGLE**  
  - **Type:** Transcriptomics-guided slide representation learning  
  - **Summary:** A modern method that uses transcriptomic supervision to improve slide-level representation learning.  
  - **Paper:** https://arxiv.org/abs/2405.11618  
  - **Code:** https://github.com/mahmoodlab/TANGLE

- **PathOmics**  
  - **Type:** Pathology-genomics multimodal transformer  
  - **Summary:** A representative multimodal transformer for fusing pathology and genomics for survival prediction.  
  - **Paper:** https://www.sciencedirect.com/science/article/pii/S1361841523000506  
  - **Code:** https://github.com/Cassie07/PathOmics

- **HE2Gene**  
  - **Type:** Image-to-RNA prediction for spatial transcriptomics  
  - **Summary:** A multi-task learning framework that predicts spot-level gene expression and pathology annotations from H&E images.  
  - **Paper:** https://academic.oup.com/bioinformatics/article/40/6/btae343/7688334  
  - **Code:** https://github.com/Microbiods/HE2Gene

- **SEAL**  
  - **Type:** Spatial transcriptomics-driven pathology FM adaptation  
  - **Summary:** A recent framework for enhancing pathology foundation models using localized spatial-expression supervision.  
  - **Paper:** https://arxiv.org/abs/2602.14177  
  - **Code:** https://github.com/mahmoodlab/SEAL

- **HEST**  
  - **Type:** Benchmark and library for histology + spatial transcriptomics  
  - **Summary:** A key dataset and benchmarking suite for multimodal histology–spatial omics learning.  
  - **Project:** https://github.com/mahmoodlab/HEST

---

## Vision-Language Models and Pathology Agents

Pathology is increasingly moving toward models that jointly reason over **image, slide context, pathology text, and report-style outputs**.

- **PathChat**  
  - **Type:** Multimodal pathology copilot  
  - **Summary:** A large-scale pathology-specific multimodal assistant trained on visual-language instructions.  
  - **Paper:** https://www.nature.com/articles/s41586-024-07618-3

- **SlideChat**  
  - **Type:** WSI-level vision-language assistant  
  - **Summary:** One of the first systems explicitly designed for gigapixel whole-slide conversational understanding.  
  - **Paper:** https://arxiv.org/abs/2410.11761  
  - **Code:** https://github.com/uni-medical/SlideChat

- **HistoGPT**  
  - **Type:** Pathology report generation model  
  - **Summary:** A vision-language model for report generation from multiple full-resolution histology slides.  
  - **Paper:** https://www.nature.com/articles/s41467-025-60014-x  
  - **Code:** https://github.com/marrlab/HistoGPT

- **WsiCaption**  
  - **Type:** WSI report generation  
  - **Summary:** A multiple-instance generation framework for pathology report generation from gigapixel slides.  
  - **Paper:** https://arxiv.org/abs/2311.16480  
  - **Code:** https://github.com/cpystan/Wsi-Caption

- **CPath-Omni**  
  - **Type:** Unified multimodal pathology foundation model  
  - **Summary:** A large multimodal model designed to unify patch- and WSI-level tasks including classification, VQA, captioning, and referring.  
  - **Paper:** https://openaccess.thecvf.com/content/CVPR2025/html/Sun_CPath-Omni_A_Unified_Multimodal_Foundation_Model_for_Patch_and_Whole_CVPR_2025_paper.html  
  - **Code:** https://github.com/PathFoundation/CPath-Omni

- **KEEP**  
  - **Type:** Knowledge-enhanced pathology foundation model  
  - **Summary:** A model that explicitly injects disease knowledge into pathology vision-language pretraining.  
  - **Project / Code:** https://github.com/MAGIC-AI4Med/KEEP

---

## Clinical Tasks and Applications

This section groups representative tasks rather than attempting to enumerate all disease-specific benchmarks.

### 1. Tumor detection and slide-level diagnosis
- **Representative benchmarks:** CAMELYON16 / CAMELYON17  
- **Representative methods:** CLAM, DSMIL, TransMIL  
- **Useful repos:**  
  - https://github.com/mahmoodlab/CLAM  
  - https://github.com/binli123/dsmil-wsi  
  - https://github.com/szc19990412/transmil

### 2. Cancer grading and subtyping
- **Representative benchmarks:** PANDA, TCGA-derived cohorts  
- **Representative methods:** HIPT, hierarchical WSI transformers, slide encoders such as CHIEF / Prov-GigaPath / TITAN  
- **Useful repos:**  
  - https://github.com/mahmoodlab/HIPT  
  - https://github.com/computationalpathologygroup/hvit  
  - https://github.com/prov-gigapath/prov-gigapath

### 3. Biomarker and mutation prediction
- **Representative direction:** slide embeddings + downstream linear probing / MIL fine-tuning / multimodal learning  
- **Representative models:** UNI, CHIEF, TITAN, Threads  
- **Useful repos:**  
  - https://github.com/mahmoodlab/UNI  
  - https://github.com/hms-dbmi/CHIEF  
  - https://github.com/mahmoodlab/TITAN

### 4. Survival and prognosis modeling
- **Representative direction:** WSI + genomics / pathology-omics fusion  
- **Representative methods:** PathOmics, HE2RNA-style molecular prediction, slide foundation model probing  
- **Useful repos:**  
  - https://github.com/Cassie07/PathOmics  
  - https://github.com/owkin/HE2RNA_code

### 5. Nuclei, cell, and tissue segmentation
- **Representative datasets:** PanNuke, NuCLS, CoNSeP  
- **Representative methods:** HoVer-Net, CellViT, NuClick  
- **Useful repos:**  
  - https://github.com/vqdang/hover_net  
  - https://github.com/TIO-IKIM/CellViT  
  - https://github.com/navidstuv/NuClick

### 6. Pathology report generation and pathology assistants
- **Representative methods:** PathChat, HistoGPT, WsiCaption, SlideChat  
- **Useful repos:**  
  - https://github.com/marrlab/HistoGPT  
  - https://github.com/cpystan/Wsi-Caption  
  - https://github.com/uni-medical/SlideChat

---

## Evaluation, Metrics, and Reproducibility

### Common evaluation axes

- **Patch-level tasks:** Accuracy, AUC, F1, Cohen’s kappa, mAP
- **Slide-level tasks:** AUC, balanced accuracy, macro F1, C-index, calibration
- **Segmentation tasks:** Dice, IoU, PQ, mPQ, AJI
- **Vision-language tasks:** captioning metrics, VQA accuracy, retrieval metrics, expert evaluation
- **Multi-omics tasks:** gene-wise correlation, ranking metrics, cross-modal retrieval, OOD generalization

### Reproducibility recommendations

- Report **WSI-level** rather than patch-level split leakage.
- Separate **internal**, **external**, and **cross-site** evaluation whenever possible.
- Control for **scanner**, **stain**, **institution**, and **specimen-type** shifts.
- Distinguish clearly between:
  - frozen feature extraction + linear probing
  - MIL fine-tuning
  - end-to-end fine-tuning
  - prompt / adapter / LoRA tuning
- For pathology FMs, always document:
  - input tile size and magnification
  - tiling strategy and tissue filtering
  - feature dimensionality
  - aggregator architecture
  - supervision granularity

### Useful benchmarking projects

- **UnPuzzle**  
  - **Paper:** https://arxiv.org/abs/2503.03152  
  - **Code:** https://github.com/Puzzle-AI/UnPuzzle

- **HEST-Benchmark**  
  - **Project:** https://github.com/mahmoodlab/HEST

- **Pathology foundation model list**  
  - **Project:** https://github.com/georg-wolflein/pathology-foundation-models

---

## Interpretability, Explainability, and Trustworthiness

Interpretability in computational pathology is not just a visualization problem; it is also about whether the model’s evidence aligns with histomorphology, biology, and pathology workflow.

### Common directions

- **Attention / saliency visualization** for MIL and slide encoders
- **Patch ranking and prototype analysis** for slide-level evidence discovery
- **Nuclei / cell-level quantification** for interpretable morphology descriptors
- **Pathology-language grounding** for report generation and pathology VQA
- **Cross-modal biological validation** using genomics or spatial transcriptomics

### Representative resources

- **CLAM** — interpretable weakly supervised WSI classification  
  - **Paper:** https://www.nature.com/articles/s41551-020-00682-w  
  - **Code:** https://github.com/mahmoodlab/CLAM

- **HE2RNA** — virtual spatialization of gene expression  
  - **Paper:** https://www.nature.com/articles/s41467-020-17678-4  
  - **Code:** https://github.com/owkin/HE2RNA_code

- **HoVer-Net** — interpretable nuclei-level segmentation and classification  
  - **Paper:** https://www.sciencedirect.com/science/article/pii/S1361841519301045  
  - **Code:** https://github.com/vqdang/hover_net

- **PathChat / HistoGPT / SlideChat** — language-grounded pathology reasoning and report generation  
  - **Paper (PathChat):** https://www.nature.com/articles/s41586-024-07618-3  
  - **Paper (HistoGPT):** https://www.nature.com/articles/s41467-025-60014-x  
  - **Paper (SlideChat):** https://arxiv.org/abs/2410.11761

---

## Resources, Toolkits, and Open-Source Projects

### Core slide IO / preprocessing / annotation tools

- **OpenSlide**  
  - **Summary:** The standard library for reading whole-slide images from multiple vendors.  
  - **Website:** https://openslide.org/  
  - **Code:** https://github.com/openslide/openslide

- **QuPath**  
  - **Summary:** One of the most widely used open-source digital pathology tools for visualization, annotation, cell detection, and analysis.  
  - **Website:** https://qupath.github.io/  
  - **Code:** https://github.com/qupath/qupath

- **WholeSlideData**  
  - **Summary:** A practical toolkit for efficient WSI sampling and training-time patch extraction.  
  - **Code:** https://github.com/DIAGNijmegen/pathology-whole-slide-data

### Python / deep learning toolkits

- **TIAToolbox**  
  - **Summary:** A mature end-to-end computational pathology toolbox for patch extraction, WSI inference, stain normalization, segmentation, and deployment.  
  - **Paper:** https://pmc.ncbi.nlm.nih.gov/articles/PMC9509319/  
  - **Code:** https://github.com/tissueimageanalytics/tiatoolbox

- **PathML**  
  - **Summary:** A general-purpose research toolkit for computational pathology pipelines and high-resolution pathology ML workflows.  
  - **Docs:** https://pathml.readthedocs.io/  
  - **Code:** https://github.com/Dana-Farber-AIOS/pathml

- **Slideflow**  
  - **Summary:** A user-friendly deep learning library for digital pathology model development and experimentation.  
  - **Code:** https://github.com/slideflow/slideflow

- **MONAI Pathology Tutorials**  
  - **Summary:** Pathology examples inside MONAI, including HoVer-Net training and pathology-specific workflows.  
  - **Project:** https://github.com/Project-MONAI/tutorials

### Curated project hubs

- **Awesome Pathology**  
  - **Project:** https://github.com/open-pathology/awesome-pathology

- **Awesome Computational Pathology Papers**  
  - **Project:** https://github.com/DearCaat/Awesome-Computational-Pathology-Papers

- **Pathology Foundation Models list**  
  - **Project:** https://github.com/georg-wolflein/pathology-foundation-models

---

## Acknowledgements

This README was reorganized around the actual structure of modern computational pathology rather than a generic AI template. The focus is on resources that are useful for:

- entering the field,
- reproducing representative baselines,
- understanding the shift from MIL to foundation models,
- and tracking the move toward multimodal and clinically grounded pathology AI.

If you find an important paper, benchmark, or open-source project missing, contributions are welcome.

---

## Citation

If you use this repository in your work, please consider citing the relevant original papers and linking back to this list.

```bibtex
@misc{awesome_computational_pathology,
  title  = {Awesome-Computational-Pathology},
  author = {Community Contributors},
  year   = {2026},
  note   = {A curated list of papers, models, datasets, and resources for computational pathology}
}
```
