from dataclasses import dataclass
import typing
import argcfg
import argparse
import sys

# Step 1: Define a configuration class with default hyperparameters
@dataclass
class TrainingConfig:
    learning_rate: float = 0.001
    batch_size: int = 32
    num_epochs: int = 10
    hidden_channels: typing.List[int] = None
    dropout: float = 0.2
    use_bn: bool = True  # Use batch normalization by default


# Step 2: Load a default configuration based on the dataset
def load_default_cfg(dataset):
    """Returns a dataset-specific default TrainingConfig."""
    if dataset == "mnist":
        return TrainingConfig(
            batch_size=64,  
            num_epochs=20   
        )
    elif dataset == "cifar10":
        return TrainingConfig(
            dropout=0.4,    
            learning_rate=0.01  
        )
    else:
        return TrainingConfig()  


if __name__ == "__main__":

    # Step 3: Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Training Configuration")

    # Define dataset argument first, as it determines the default config
    parser.add_argument("--dataset", type=str, help="Dataset name")

    # Dynamically add arguments based on TrainingConfig fields
    argcfg.add_args_by_config_class(parser, TrainingConfig, verbose=True)


    # Uncomment the following block if you want to test this script without manually passing CLI arguments
    # This simulates running:
    # python demo_argcfg.py --dataset cifar10 --num_epochs 50 --hidden_channels 32,64,128 --use_bn False
    # Note that, you do not need to pass all the arguments, only the ones you want to override

    # cmd = "--dataset cifar10 --num_epochs 50 --hidden_channels 32,64,128 --use_bn False"
    # sys.argv += cmd.split()


    # Step 4: Parse command-line arguments
    args = parser.parse_args()

    # Step 5: Load the default configuration based on the dataset
    config = load_default_cfg(args.dataset)

    # Step 6: Override default config values with parsed arguments
    argcfg.combine_args_into_config(config, args, verbose=True)

    # Step 7: Display the final configuration after merging defaults & parsed arguments
    print("Final Configuration:")
    print(config)
