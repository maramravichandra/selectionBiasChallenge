
import numpy as np
import matplotlib.pyplot as plt

def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Assembles all four panels into a professional-looking meme.

    Args:
        original_img: The original image.
        stipple_img: The stippled image.
        block_letter_img: The block letter "S" image.
        masked_stipple_img: The masked stippled image.
        output_path: The path to save the output meme.
        dpi: The DPI for the output image.
        background_color: The background color of the meme.
    """
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    fig.patch.set_facecolor(background_color)

    images = [original_img, stipple_img, block_letter_img, masked_stipple_img]
    titles = ["Reality", "Your Model", "Selection Bias", "Estimate"]

    for ax, img, title in zip(axes, images, titles):
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor('black')
            spine.set_linewidth(2)

    plt.tight_layout(pad=3.0)
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close(fig)

