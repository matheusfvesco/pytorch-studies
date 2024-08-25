# Pytorch Studies

A collection of Jupyter notebooks designed to help me (and others) learn PyTorch and check my learning through practical exercises and projects

## Colab badges

Use the following badges to easily access the notebooks in Google Colab.

<!-- BADGES -->
| Name | Colab|
| ---- | ---- |
| torchvision/datasets.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/datasets.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/detection-finetune.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/detection-finetune.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/utilities.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/utilities.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/transforms_v2.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/transforms_v2.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/classification-finetune.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/classification-finetune.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/detection-inference.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/detection-inference.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/classification-inference.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/classification-inference.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| torchvision/custom-datasets.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/torchvision/custom-datasets.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/datasets.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/datasets.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/dataloaders.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/dataloaders.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/layers.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/layers.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/checkpoints.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/checkpoints.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/networks.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/networks.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/tensor_operations.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/tensor_operations.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
| basics/tensors.ipynb | <a href=https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/basics/tensors.ipynb target=_parent><img src=https://colab.research.google.com/assets/colab-badge.svg alt=Open In Colab/></a>|
<!-- SEGDAB -->

## Development

Use the provided devcontainer to run the colabs locally. Beaware that the devcontainer is based on the google colab image from Google, and therefore the image requires ~30-40 GB of disk space.

### Creating the badges

Before committing, ensure you run `generate_badges.sh` to update the README.md with all of the colabs's badges:

```bash
./generate_badges.sh
```
