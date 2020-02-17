# DeepSphere: towards an equivariant graph-based spherical CNN

[Nathanaël Perraudin][nath], [Michaël Defferrard][mdeff], [Tomasz Kacprzak][tomek], [Raphael Sgier][raphael]\
Representation Learning on Graphs and Manifolds (RLGM) workshop, International Conference on Learning Representations (ICLR), 2019

[nath]: https://perraudin.info
[mdeff]: https://deff.ch
[tomek]: https://www.ipa.phys.ethz.ch/people/person-detail.MjEyNzM5.TGlzdC82NjQsNTkxMDczNDQw.html
[raphael]: https://www.ipa.phys.ethz.ch/people/person-detail.MTcyNDY3.TGlzdC82NjQsNTkxMDczNDQw.html

> Spherical data is found in many applications.
> By modeling the discretized sphere as a graph, we can accommodate non-uniformly distributed, partial, and changing samplings.
> Moreover, graph convolutions are computationally more efficient than spherical convolutions.
> As equivariance is desired to exploit rotational symmetries, we discuss how to approach rotation equivariance using the graph neural network introduced in Defferrard et al. (2016).
> Experiments show good performance on rotation-invariant learning problems.
> Code and examples are available at https://github.com/SwissDataScienceCenter/DeepSphere.

**PDF available at [arxiv], [workshop], [infoscience].**\
Related: [poster], [code], [data], [blog], [slides].

[arxiv]: https://arxiv.org/abs/1904.05146
[workshop]: https://rlgm.github.io/papers/71.pdf
[infoscience]: https://infoscience.epfl.ch
[poster]: https://doi.org/10.5281/zenodo.2839355
[code]: https://github.com/SwissDataScienceCenter/DeepSphere
[data]: https://doi.org/10.5281/zenodo.1303271
[blog]: https://datascience.ch/deepsphere-a-neural-network-architecture-for-spherical-data
[slides]: https://doi.org/10.5281/zenodo.3243380

## Compilation

Compile the latex source into a PDF with `make`.

## Figures

All the figures, along with the code and data to reproduce them, are in the [`figure`](figures/) folder.
While the PDFs are stored, they can be regenerated with `make figures`.
