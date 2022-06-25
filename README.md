# Chinese-Noisy-Text

This repository stores the code of the data augmentation method from Chinese word and character levels, which adds noise to words and characters in redundant, missing, selection and ordering respectively.

## Requirements

`pip install -r requirements.txt`

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
@misc{Xia2022,
  author = {Peng Xia},
  title = {Chinese-Noisy-Text},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Richard88888/Chinese-Noisy-Text}},
  commit = {602a630730ce8b61ea8882251e5516ad1930fa43}
}
@inproceedings{tang2021基于字词粒度噪声数据增强的中文语法纠错,
  title={基于字词粒度噪声数据增强的中文语法纠错 (Chinese Grammatical Error Correction enhanced by Data Augmentation from Word and Character Levels)},
  author={Tang, Zecheng and Ji, Yixin and Zhao, Yibo and Li, Junhui},
  booktitle={Proceedings of the 20th Chinese National Conference on Computational Linguistics},
  pages={813--824},
  year={2021}
}
```

## Notes

Do not hesitate to contact me if you need some help, need a feature or see some bug

Feel free and welcome to contribute
