# Reviews of DeepShere at the ICLR 2019 Workshop on Representation Learning on Graphs and Manifolds

Congratulations! We are happy to inform you that your paper has been accepted to the ICLR 2019 Workshop on Representation Learning on Graphs and Manifolds. All papers will be presented as posters, and we will follow-up with additional presentation details in the coming days.

## Reviewer #1

4. Overall recommendation
Accept

5. Reviewer Confidence
Reviewer is confident but not certain

6. Please provide a detailed review consisting of the following: summary, justification for scores, at least 2 strong points and areas for improvement

This paper studied the prediction problem on spheres. Graphs provide a nice representation for such prediction problems because of its equivariance and invariance properties. The particular variant of graph convnet proposed in Defferrard et al. 2016 is used. Converting signals on a sphere into a graph is not a trivial problem as regular sampling (sampling uniformly spaced points) on spheres is impossible, therefore some discussion of the sampling and the equivariance properties of the spherical convolutions are also presented. The model is shown to perform consistently better than 2D convnets where the spherical signal is converted into flat images, and also better than linear SVMs on extracted features, on a task of classifying cosmological convergence maps.

Overall I think the choice of graph neural networks for prediction problems on spheres makes a lot of sense. I also really appreciate the discussion of sampling points on the sphere and constructing the graph structure in the paper, as this is usually assumed to be given when studying machine learning models on graphs. This part however is a bit difficult to understand (the compact format of 4 pages probably made the problem worse) for someone lacking enough background.

One related work that is missed by the authors is “Spectral Networks and Deep Locally Connected Networks on Graphs” by Bruna et al. from 2013, which already tried to do classification of data on spheres, through (spectral) graph convolutions. The relation to this work should be discussed.

Another question I had was, if we can control the sampling process, would it be beneficial to get multiple samples, make predictions and average the predictions? This way we may be able to reduce the variance and get closer to equivariance / invariance.

One last point, this paper made a few reference to the “Deepsphere” paper posted on arXiv (e.g. “In this contribution we present DeepShere (anonymous 2018)”). I don’t know if this violates the blind review principles.

## Reviewer #4

4. Overall recommendation
Strong accept

5. Reviewer Confidence
Reviewer is confident but not certain

6. Please provide a detailed review consisting of the following: summary, justification for scores, at least 2 strong points and areas for improvement

-=GENERAL=-
The paper proposes a new approach to deal with spherical input data. The idea is to use a graph-based approximation to a sphere and then apply a graph neural network. The key component of the model is HEALPix, however, other sampling methods could be used. Importantly, the model is (approximately) rotation equivariant and also rotation invariant if a global average pooling is used.

Pros:
+ The paper is well-motivated.
+ The paper is well-written.
+ The results are promising.

Cons:
- (Minor) I miss some references to works on (hyper)spherical representation learning:
* Davidson, Tim R., et al. "Hyperspherical variational auto-encoders." arXiv preprint arXiv:1804.00891 (2018).
* Oh, Changyong, Kamil Adamczewski, and Mijung Park. "Radial and Directional Posteriors for Bayesian Neural Networks." arXiv preprint arXiv:1902.02603 (2019).
* Falorsi, Luca, et al. "Reparameterizing Distributions on Lie Groups." arXiv preprint arXiv:1903.02958 (2019).
* Mathieu, Emile, et al. "Hierarchical Representations with Poincar\'e Variational Auto-Encoders." arXiv preprint arXiv:1901.06033 (2019).

-=REMARK=-
The authors violated a double blind reviewing process by providing a link to their github repository. Nevertheless, I find the paper very interesting and, thus, I vote for accepting.
