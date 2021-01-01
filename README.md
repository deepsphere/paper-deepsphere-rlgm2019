# DeepSphere: towards an equivariant graph-based spherical CNN

[Nathanaël Perraudin](https://perraudin.info),
[Michaël Defferrard](https://deff.ch),
[Tomasz Kacprzak](https://www.ipa.phys.ethz.ch/people/person-detail.MjEyNzM5.TGlzdC82NjQsNTkxMDczNDQw.html),
[Raphael Sgier](https://www.ipa.phys.ethz.ch/people/person-detail.MTcyNDY3.TGlzdC82NjQsNTkxMDczNDQw.html) \
Representation Learning on Graphs and Manifolds (RLGM) workshop at the International Conference on Learning Representations (ICLR), 2019

> Spherical data is found in many applications.
> By modeling the discretized sphere as a graph, we can accommodate non-uniformly distributed, partial, and changing samplings.
> Moreover, graph convolutions are computationally more efficient than spherical convolutions.
> As equivariance is desired to exploit rotational symmetries, we discuss how to approach rotation equivariance using the graph neural network introduced in Defferrard et al. (2016).
> Experiments show good performance on rotation-invariant learning problems.
> Code and examples are available at https://github.com/deepsphere.

```
@inproceedings{deepsphere_rlgm,
  title = {{DeepSphere}: towards an equivariant graph-based spherical {CNN}},
  author = {Defferrard, Micha\"el and Perraudin, Nathana\"el and Kacprzak, Tomasz and Sgier, Raphael},
  booktitle = {ICLR Workshop on Representation Learning on Graphs and Manifolds},
  year = {2019},
  archiveprefix = {arXiv},
  eprint = {1904.05146},
  url = {https://arxiv.org/abs/1904.05146},
}
```

## Resources

PDF available at [arXiv] and the [workshop].

Related: [poster], [code].

[arXiv]: https://arxiv.org/abs/1904.05146
[workshop]: https://rlgm.github.io/papers/71.pdf
[poster]: https://doi.org/10.5281/zenodo.2839355
[code]: https://github.com/deepsphere

## Compilation

Compile the latex source into a PDF with `make`.
Run `make clean` to remove temporary files and `make arxiv.zip` to prepare an archive to be uploaded on arxiv.

## Figures

All the figures, along with the code and data to reproduce them, are in the [`figures`](figures/) folder.
While the PDFs are stored, they can be regenerated with `make figures`.

## Reviews

The workshop reviews are found in [`reviews.md`](reviews.md).
