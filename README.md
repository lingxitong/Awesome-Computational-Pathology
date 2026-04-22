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
- **OV-Bevacizumab** — multi-modal dataset for predicting ovarian cancer response to Bevacizumab treatment. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data-b31b1b.svg)](https://www.nature.com/articles/s41597-022-01127-6)
- **BCNB** — massive breast cancer nodule and biomarker dataset for AI-assisted diagnosis. [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://bupt-ai-cz.github.io/BCNB/)
- **MUT-HET-RCC** — dataset for exploring intra-tumor heterogeneity and mutation prediction in renal cell carcinoma. [![Dataset](https://img.shields.io/badge/Dataset-Figshare-orange.svg)](https://doi.org/10.25452/figshare.plus.c.5983795)
- **HER2-Tumor-ROIs** — regions of interest annotated specifically for HER2 scoring in breast cancer. [![Dataset](https://img.shields.io/badge/Dataset-TCIA-orange.svg)](https://www.cancerimagingarchive.net/collection/her2-tumor-rois/)
- **NADT-Prostate** — dataset focusing on neoadjuvant androgen deprivation therapy in prostate cancer. [![Paper](https://img.shields.io/badge/Paper-MedRxiv-b31b1b.svg)](https://www.medrxiv.org/content/10.1101/2020.09.29.20199711v1)
- **EBRAINS** — ultra-high-resolution comprehensive brain mapping whole-slide images. [![Dataset](https://img.shields.io/badge/Dataset-EBRAINS-orange.svg)](https://doi.org/10.25493/WQ48-ZGX)
- **VisioMel** — challenge dataset for melanoma prediction and lymph node metastasis forecasting. [![Dataset](https://img.shields.io/badge/Dataset-DrivenData-orange.svg)](https://www.drivendata.org/competitions/148/visiomel-melanoma/)
- **IMP** — robust multi-institutional pathology dataset for cervical and diverse tissue analysis. [![Dataset](https://img.shields.io/badge/Dataset-INESC%20TEC-orange.svg)](https://rdm.inesctec.pt/dataset/nis-2023-008)
- **Selected Cohorts**: [BRCA](https://www.cancerimagingarchive.net/collection/cptac-brca/) (Breast), [LUAD/LSCC](https://www.cancerimagingarchive.net/collection/cptac-luad/) (Lung), [GBM](https://www.cancerimagingarchive.net/collection/cptac-gbm/) (Brain), [CCRCC](https://www.cancerimagingarchive.net/collection/cptac-ccrcc/) (Kidney), [COAD](https://www.cancerimagingarchive.net/collection/cptac-coad/) (Colon), [UCEC](https://www.cancerimagingarchive.net/collection/cptac-ucec/) (Uterine), [HNSC](https://www.cancerimagingarchive.net/collection/cptac-hnsc/) (Head & Neck).
- **CoNIC** — massive colon nuclei identification and counting challenge dataset. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841522000755) [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/6559981)
- **PAIP** — comprehensive pathology AI platform challenge cohorts for liver cancer segmentation and survival prediction. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521000577) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://paip2019.grand-challenge.org/)
- **BACH** — grand challenge dataset for breast cancer histology image classification and segmentation. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841518301789) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://iciar2018-challenge.grand-challenge.org/)
- **BCI** — breast cancer immunohistochemical dataset for translating H&E to IHC stained images. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_Translating_From_HE_to_IHC_A_New_Trajectory_for_Translational_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bupt-ai-cz/BCI)
- **EBHI-Seg** — a comprehensive dataset for tumor segmentation in H&E stained digestive system tissues. [![Paper](https://img.shields.io/badge/Paper-Sci%20Data-b31b1b.svg)](https://www.nature.com/articles/s41597-022-01435-y) [![Dataset](https://img.shields.io/badge/Dataset-Figshare-orange.svg)](https://figshare.com/articles/dataset/EBHI-Seg/19602495)
- **HEROHE** — a large dataset for predicting HER2 receptor status in breast cancer directly from routine H&E WSIs. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521002369) [![Dataset](https://img.shields.io/badge/Dataset-Website-orange.svg)](https://herohe.inesctec.pt/)
- **SICAPv2** — prostate cancer grading dataset with expert-level gleason score annotations. [![Paper](https://img.shields.io/badge/Paper-IEEE%20JBHI-1f77b4.svg)](https://ieeexplore.ieee.org/document/9144365) [![Dataset](https://img.shields.io/badge/Dataset-Mendeley-orange.svg)](https://data.mendeley.com/datasets/9xxm58dvs3/1)
- **UniToPatho** — colon cancer dataset focusing on overcoming class imbalance and domain shift. [![Paper](https://img.shields.io/badge/Paper-ECCV%202020-b31b1b.svg)](https://arxiv.org/abs/2009.00650) [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/3934241)
- **NCT-CRC-HE-100K** — 100,000 H&E-stained colorectal tissue patches across 9 tissue classes; de facto standard for benchmarking patch-level encoders and foundation models. [![Dataset](https://img.shields.io/badge/Dataset-Zenodo-orange.svg)](https://zenodo.org/record/1214456)
- **GlaS** — Gland Segmentation in Colon Histology Images Challenge (MICCAI 2015); canonical benchmark for glandular structure instance segmentation. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841516301736) [![Dataset](https://img.shields.io/badge/Dataset-Warwick-orange.svg)](https://warwick.ac.uk/fac/cross_fac/tia/data/glascontest/)
- **MoNuSeg** — Multi-Organ Nucleus Segmentation benchmark covering 30 patients across 7 organs; widely adopted for nuclei segmentation and cross-organ generalization studies. [![Paper](https://img.shields.io/badge/Paper-IEEE%20TMI-1f77b4.svg)](https://ieeexplore.ieee.org/document/8880654) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monuseg.grand-challenge.org/)
- **MoNuSAC2020** — Multi-Organ Nuclei Segmentation and Classification challenge extending MoNuSeg with 4 nuclei categories (epithelial, lymphocyte, macrophage, neutrophil). [![Paper](https://img.shields.io/badge/Paper-IEEE%20TMI-1f77b4.svg)](https://ieeexplore.ieee.org/document/9446924) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://monusac-2020.grand-challenge.org/)
- **TissueNet** — large-scale cell segmentation benchmark spanning multiplexed tissue imaging modalities (CyCIF, CODEX, MIBI-TOF, IMC); enables evaluation of cross-platform generalisation. [![Paper](https://img.shields.io/badge/Paper-Nature%20Methods-1f77b4.svg)](https://www.nature.com/articles/s41592-021-01249-6) [![Dataset](https://img.shields.io/badge/Dataset-DeepCell-orange.svg)](https://datasets.deepcell.org/)
- **OCELOT** — Overlapping Cell on Tissue dataset coupling cell detection with tissue-region context; MICCAI 2023 grand challenge. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Ryu_OCELOT_Overlapping_Cell_on_Tissue_Dataset_for_Histopathology_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lunit-io/ocelot-benchmark)
- **TCGA-TIL Maps** — spatial tumor-infiltrating lymphocyte maps across 13 TCGA cancer types, enabling pan-cancer immune landscape analysis directly from routine H&E. [![Paper](https://img.shields.io/badge/Paper-Cell%20Reports-b31b1b.svg)](https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31438-5) [![Dataset](https://img.shields.io/badge/Dataset-TCIA-orange.svg)](https://www.cancerimagingarchive.net/analysis-result/til-maps/)
- **DigestPath** — Digestive-system Pathology Analysis challenge (MICCAI 2019) covering colonoscopy tissue segmentation and malignancy classification. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841521003571) [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://digestpath2019.grand-challenge.org/)
- **AGGC2022** — Automated Gleason Grading Challenge 2022; large-scale prostate cancer Gleason scoring from whole-slide images with expert-consensus annotations. [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://aggc22.grand-challenge.org/)
- **TIGER** — Tumor InfiltratinG lymphocytes in breast canceR grand challenge covering TIL region segmentation, detection, and WSI-level scoring. [![Dataset](https://img.shields.io/badge/Dataset-Grand%20Challenge-orange.svg)](https://tiger.grand-challenge.org/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DIAGNijmegen/tiger-challenge-eval)


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
- **ViLa-MIL** — dual-scale vision-language multiple instance learning for WSI classification. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_ViLa-MIL_Dual-scale_Vision-Language_Multiple_Instance_Learning_for_Whole_Slide_Image_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiangbo-Shi/ViLa-MIL)
- **SI-MIL** — taming deep MIL for self-interpretability in gigapixel histopathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Bhattacharya_SI-MIL_Taming_Deep_MIL_for_Self-Interpretability_in_Gigapixel_Histopathology_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/bmi-imaginelab/SI-MIL)
- **FG-VSI** — generalizable WSI classification with fine-grained visual-semantic interaction. [![Paper](https://img.shields.io/badge/Paper-CVPR%202024-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Generalizable_Whole_Slide_Image_Classification_with_Fine-Grained_Visual-Semantic_Interaction_CVPR_2024_paper.html)
- **LNPL-MIL** — learning from noisy pseudo labels for promoting MIL in whole slide images. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Shao_LNPL-MIL_Learning_from_Noisy_Pseudo_Labels_for_Promoting_Multiple_Instance_ICCV_2023_paper.html)
- **MILBooster** — dual-scale multi-stage MIL framework from the perspectives of distribution, correlation, and magnification. [![Paper](https://img.shields.io/badge/Paper-ICCV%202023-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Qu_Boosting_Whole_Slide_Image_Classification_from_the_Perspectives_of_Distribution_ICCV_2023_paper.html)
- **ZoomMIL** — differentiable zooming for multiple instance learning on whole-slide images. [![Paper](https://img.shields.io/badge/Paper-ECCV%202022-b31b1b.svg)](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136810689.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histocartography/zoommil)
- **IBMIL** — interpretable and intervention-based MIL for overcoming confounding in WSI. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Lin_Interventional_Multi-Instance_Learning_with_Deconfounded_Instance-Level_Prediction_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/TencentAILabHealthcare/IBMIL)
- **ReMix** — a general multi-instance learning data augmentation method for WSI. [![Paper](https://img.shields.io/badge/Paper-ICCV%202021-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Yang_ReMix_Towards_Image_Mixup_for_Whole_Slide_Image_Classification_ICCV_2021_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Jiawei-Yang/ReMix)
- **PromptMIL** — prompting language-image models for multi-instance learning in pathology. [![Paper](https://img.shields.io/badge/Paper-MICCAI%202023-b31b1b.svg)](https://arxiv.org/abs/2303.03362) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Zhenghui-Wu/PromptMIL)
- **Clinical-grade WSI** — Campanella et al., 2019. Weakly supervised deep learning trained on 44,732 whole-slide images achieving clinical-grade accuracy for prostate, skin, and cervical cancer detection; landmark proof of concept for large-scale weakly supervised pathology. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0508-1)
- **DeepAttnMISL** — attention-guided deep MIL using multi-scale patch clustering for whole-slide-level cancer survival prediction; among the first to demonstrate cross-magnification feature integration for prognosis. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841520300487) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uta-smile/DeepAttnMISL)
- **CAMEL** — weakly supervised histopathology image segmentation from slide-level labels via class activation maps and expectation-maximization; demonstrates pixel-level supervision without patch annotations. [![Paper](https://img.shields.io/badge/Paper-ICCV%202019-b31b1b.svg)](https://openaccess.thecvf.com/content_ICCV_2019/html/Li_Camel_A_Weakly_Supervised_Learning_Framework_for_Histopathology_Image_Segmentation_ICCV_2019_paper.html)
- **S4MIL** — structured state space sequence models for MIL in digital pathology; achieves strong performance with linear complexity through selective state-space aggregation. [![Paper](https://img.shields.io/badge/Paper-MIDL%202023-b31b1b.svg)](https://proceedings.mlr.press/v227/fillioux24a.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/MICS-Lab/s4mil)
- **GTP** (Graph-Transformer for Pathology) — a graph-transformer framework fusing graph representations of WSIs with vision transformers for efficient and interpretable WSI-level classification. [![Paper](https://img.shields.io/badge/Paper-IEEE%20TMI%202022-1f77b4.svg)](https://ieeexplore.ieee.org/document/9779215) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/vkola-lab/tmi2022)

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
- **RetCCL** — clustering-guided contrastive learning for whole-slide image retrieval. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841522002572) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/Xiyue-Wang/RetCCL)
- **CS-CO** — cross-stain and cross-organ self-supervised learning for pathology. [![Paper](https://img.shields.io/badge/Paper-CVPR%202022-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Cross-Stain_and_Cross-Organ_Self-Supervised_Learning_for_Computational_Pathology_CVPR_2022_paper.html)
- **BiomedCLIP** — biomedical vision-language foundation model from 15M image-text pairs. [![Paper](https://img.shields.io/badge/Paper-Nature%20Methods-1f77b4.svg)](https://www.nature.com/articles/s41592-024-02206-1) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/microsoft/BiomedCLIP)
- **HistoSSL** — self-supervised learning for histological image analysis at scale. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-023-40004-9) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/owkin/HistoSSLscaling)
- **Quilt-1M** — one million histopathology image-text pairs curated from YouTube and social media for pathology vision-language pretraining; enables strong zero-shot performance on diverse pathology tasks. [![Paper](https://img.shields.io/badge/Paper-NeurIPS%202023-6A5ACD.svg)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/775ec578876fa6812c062644964b9870-Abstract-Datasets_and_Benchmarks.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/wisdomikezogwo/quilt1m)
- **REMEDIS** — robust and efficient medical imaging with self-supervised pretraining; demonstrates that large-scale natural image pretraining with medical fine-tuning achieves state-of-the-art on pathology benchmarks. [![Paper](https://img.shields.io/badge/Paper-Nature%20BME-1f77b4.svg)](https://www.nature.com/articles/s41551-023-01049-7) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/google-research/medical-ai-research-foundations)
- **Virchow2** — second-generation Virchow pathology FM from Paige AI with improved multi-magnification tile representations trained on a significantly expanded and diverse WSI corpus. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2408.00738) [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/paige-ai/Virchow2)
- **UNI2-h** — next-generation UNI (Mahmood Lab) trained at larger scale for further improvements in patch-level representation quality and downstream task transfer. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/MahmoodLab/UNI2-h)
- **Benchmarking SSL on Pathology** — Kang et al., CVPR 2023. First comprehensive benchmarking of 7 SSL methods (DINO, iBOT, SimCLR, MoCo, etc.) on 7 diverse pathology datasets; releases trained pathology-specific encoders and establishes iBOT-style training as the top-performing paradigm. [![Paper](https://img.shields.io/badge/Paper-CVPR%202023-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Kang_Benchmarking_Self-Supervised_Learning_on_Diverse_Pathology_Datasets_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lunit-io/benchmark-ssl-pathology)

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
- **SlideGraph+** — whole-slide graph neural network for HER2 status prediction directly from WSIs; demonstrates that slide-level graph topology outperforms bag-based MIL for biomarker tasks. [![Paper](https://img.shields.io/badge/Paper-MedIA-b31b1b.svg)](https://www.sciencedirect.com/science/article/pii/S1361841522001189) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/histocartography/SlideGraph)
- **UNI (slide-level)** — UNI patch embeddings aggregated via multiple MIL heads provide state-of-the-art slide-level classification, subtyping, and survival prediction across 34 computational pathology tasks. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02857-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/UNI)
- **CONCH (slide encoder)** — CONCH patch embeddings support both zero-shot and few-shot slide classification via text-guided scoring; forms the patch backbone for the TITAN slide-level foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)

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

- **PathChat** — multimodal generative AI copilot for human pathology. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-07618-3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/DeepReasoning/aihealth)
- **SlideChat** — whole-slide pathology vision-language assistant. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.11761) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/uni-medical/SlideChat)
- **CONCH** — caption-aligned pathology VLM backbone. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)
- **MUSK** — unified masked multimodal pathology foundation model. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-024-08437-2) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/lilab-stanford/MUSK)
- **HistoGPT** — report generation from gigapixel whole-slide images. [![Paper](https://img.shields.io/badge/Paper-Nature%20Communications-1f77b4.svg)](https://www.nature.com/articles/s41467-025-60014-x) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/marrlab/HistoGPT)
- **PathGen-1.6M** — large-scale pathology image-text dataset generated via multi-agent collaboration. [![Paper](https://img.shields.io/badge/Paper-OpenReview-b31b1b.svg)](https://openreview.net/forum?id=rFpZnn11gj) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/PathGen-1.6M)
- **PathGen-LLaVA** — pathology instruction-tuned model built on PathGen-1.6M. [![Model](https://img.shields.io/badge/Model-HuggingFace-yellow.svg)](https://huggingface.co/jamessyx/PathGen-LLaVA)
- **PathAsst** — generative foundation AI assistant for pathology. [![Paper](https://img.shields.io/badge/Paper-AAAI%202024-b31b1b.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/28308)
- **CPath-Omni** — unified multimodal FM across patch and slide scales. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.12077) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathFoundation/CPath-Omni)
- **PathMMU** — benchmark for pathology large multimodal models. [![Paper](https://img.shields.io/badge/Paper-arXiv-b31b1b.svg)](https://arxiv.org/abs/2401.16355) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/PathMMU-Benchmark/PathMMU)
- **PathBench** — benchmark for patch- and WSI-level pathology image understanding by LMMs. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/superjamessyx/PathBench)
- **Patho-R1** — multimodal reasoning-focused pathology assistant. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/wenchuan-zhang/patho-r1)
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
- **STAMP** — Kather Lab's standardized end-to-end clinical AI pipeline; connects slide-level FM features (UNI, CONCH, etc.) to oncology biomarker discovery, treatment response prediction, and patient stratification; widely adopted as a community clinical benchmark for reproducing and comparing FM-based clinical analyses. [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/KatherLab/STAMP)
- **Pan-cancer Genetic Alterations** — Kather et al., Nature Cancer 2020. Deep learning predicts clinically actionable genetic alterations (TMB, MSI, CNV, driver mutations) across 32 cancer types directly from H&E WSIs. [![Paper](https://img.shields.io/badge/Paper-Nature%20Cancer-1f77b4.svg)](https://www.nature.com/articles/s43018-020-0087-6) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/jnkather/DeepHistology)
- **CRC Outcome Prediction** — Skrede et al., The Lancet 2020. Deep learning predicts relapse-free survival from colorectal cancer H&E images in two large independent cohorts; landmark study on clinical survival endpoints from routine pathology. [![Paper](https://img.shields.io/badge/Paper-The%20Lancet-1f77b4.svg)](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(19)32998-8/fulltext)
- **PORPOISE** — Chen et al., Cancer Cell 2022. Pan-cancer integrative histology-genomic analysis via multimodal deep learning across 14 cancer types; simultaneously models slide morphology and molecular profiles for survival prediction. [![Paper](https://img.shields.io/badge/Paper-Cancer%20Cell-1f77b4.svg)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(22)00317-8) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PORPOISE)
- **AI Prostate Cancer Grading** — Strom et al., Lancet Oncology 2020. Population-based diagnostic study showing AI matches specialist-level performance in Gleason grading of prostate cancer biopsies from >6,000 patients. [![Paper](https://img.shields.io/badge/Paper-Lancet%20Oncology-1f77b4.svg)](https://www.thelancet.com/journals/lanonc/article/PIIS1470-2045(19)30738-7/fulltext)
- **TOAD** — Lu et al., Nature 2021. AI-based pathology predicts tumor origins for cancers of unknown primary across 22 tumor types from routine H&E; trained and validated on 22,000+ WSIs. [![Paper](https://img.shields.io/badge/Paper-Nature-1f77b4.svg)](https://www.nature.com/articles/s41586-021-03512-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/TOAD)
- **Multi-cancer Survival DL** — Wulczyn et al., npj Digital Medicine 2021. Deep learning prognostic models from H&E outperform pathologist staging for overall survival prediction in 10+ TCGA cancer types. [![Paper](https://img.shields.io/badge/Paper-npj%20Digital%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41746-020-00376-2)
- **CONCH Clinical** — zero-shot classification and retrieval via CONCH enables pathologist-level cancer subtyping and biomarker assessment without task-specific training. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-024-02856-4) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/CONCH)
- **Pathomic Fusion (TMI)** — Chen et al., IEEE TMI 2022. Integrates histology graph features and genomic signatures via co-attention for grade classification and survival prediction; foundational multimodal pathology paper. [![Paper](https://img.shields.io/badge/Paper-IEEE%20TMI-1f77b4.svg)](https://ieeexplore.ieee.org/document/9706562) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mahmoodlab/PathomicFusion)
- **TCGA Immune Landscape** — Saltz et al., Cell Reports 2018. Systematic mapping of TIL spatial patterns across 13 TCGA cancer types using deep learning; establishes histology-based immune profiling as a standard clinical task. [![Paper](https://img.shields.io/badge/Paper-Cell%20Reports-b31b1b.svg)](https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31438-5)
- **MSI from H&E (GI)** — Kather et al., 2019. Proof-of-principle that microsatellite instability status can be directly read from routine H&E slides with deep learning, avoiding reflex IHC/PCR testing. [![Paper](https://img.shields.io/badge/Paper-Nature%20Medicine-1f77b4.svg)](https://www.nature.com/articles/s41591-019-0462-y)

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
