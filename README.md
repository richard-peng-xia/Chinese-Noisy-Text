# Chinese-Noisy-Text
[![OSCS Status](https://www.oscs1024.com/platform/badge/Richard88888/Chinese-Noisy-Text.svg?size=small)](https://www.oscs1024.com/project/Richard88888/Chinese-Noisy-Text?ref=badge_small) ![Github stars](https://img.shields.io/github/stars/Richard88888/Chinese-Noisy-Text.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

This repository stores the code of the data augmentation method from Chinese word and character levels, which adds noise to words and characters in redundant, missing, selection and ordering respectively.

## Requirements & Datasets

`pip install -r requirements.txt`

Due to copyright restrictions, the two folders have not been uploaded. You can download them from these two links below if you need them. 

[ChineseHomophones](https://github.com/LiangsLi/ChineseHomophones) | [SimilarCharacter](https://github.com/contr4l/SimilarCharacter)

## Usage

I've implemented the 5 noise functions described in the paper:

1. Delete words with given probability (default is 0.163)
2. Replace words by a similar words and homophone with given probability (default is 0.163)
3. Swap words up to a certain range (default range is 0.163)
4. Repeat words with given probability (default is 0.163)
5. Select any of the above noise functions at random

I set the error rate of each time as 16.3%, which can maintain the error rate of the corpus after double noise at 30% (calculated according to mathematical expectation).

Example of simple usage

`bash noise.sh`

Example of complete usage

`python add_noise/add_noise.py --input input_file_path --redundant_probability 0.2  --selection_probability 0.2 --missing_probability 0.2  --ordering_probability 0.2 --comprehensive_error_probability 0.2`

## Results
![image](https://user-images.githubusercontent.com/68063744/175760956-5045590b-daa8-44c2-8073-7f2efba98ab0.png)
*Examples of noisy texts*

I've run Chinese grammatical error correction experiments on Chinese Wikipedia corpus, using all available parallel data.

I added noise to it using this repo, giving the following results on NLPCC 2018 test set. All results are $F_{0.5}$ Scores.

The table below reports a Transformer model identical to the "base model" in [Vaswani et al. (2017)](https://arxiv.org/pdf/1706.03762.pdf).

| Model          | $F_{0.5}$  |
| -------------- | ------------- |
| baseline       | 33.17         |
| baseline+noise | **35.55**    |

*Transformer base model*

## Reference

```
@article{xia2022chinese,
  title={Chinese grammatical error correction based on knowledge distillation},
  author={Xia, Peng and Zhou, Yuechi and Zhang, Ziyan and Tang, Zecheng and Li, Juntao},
  journal={arXiv preprint arXiv:2208.00351},
  year={2022}
}
@software{peng_richard_xia_2022_7025129,
  author       = {Peng(Richard) Xia},
  title        = {Richard88888/Chinese-Noisy-Text: v1.0},
  month        = aug,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {doi},
  doi          = {10.5281/zenodo.7025129},
  url          = {https://doi.org/10.5281/zenodo.7025129}
}
@inproceedings{tang2021基于字词粒度噪声数据增强的中文语法纠错,
  title={基于字词粒度噪声数据增强的中文语法纠错 (Chinese Grammatical Error Correction enhanced by Data Augmentation from Word and Character Levels)},
  author={Tang, Zecheng and Ji, Yixin and Zhao, Yibo and Li, Junhui},
  booktitle={Proceedings of the 20th Chinese National Conference on Computational Linguistics},
  pages={813--824},
  year={2021}
}

```
<!-- @misc{Xia2022ChineseNoisyText,
  author = {Peng Xia},
  title = {Chinese-Noisy-Text},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Richard88888/Chinese-Noisy-Text}}
} --!>


## Notes

Do not hesitate to contact me if you need some help, need a feature or see some bug

Feel free and welcome to contribute
