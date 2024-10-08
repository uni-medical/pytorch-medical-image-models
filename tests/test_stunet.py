from medim.models import create_model
import torch
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestSTUNet_small():

    def test_stunet_s_simple_example(self):
        model = create_model("STU-Net-S")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_s_with_input_args(self):
        model = create_model("STU-Net-S", input_channels=3)
        input_tensor = torch.randn(1, 3, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_s_with_output_args(self):
        model = create_model("STU-Net-S", num_classes=3)
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 3, 128, 128, 128])

    def test_stunet_s_with_local_checkpoint(self):
        model = create_model("STU-Net-S",
                             pretrained=True,
                             checkpoint_path=os.path.join("tests", "data",
                                                          "Totalseg_small_ep4k.model"))
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_s_without_local_checkpoint(self):
        with pytest.raises(FileNotFoundError):
            create_model("STU-Net-S",
                         pretrained=True,
                         checkpoint_path=os.path.join("xxx_ep4k.model"))

    def test_stunet_s_with_wrong_local_checkpoint(self):
        with pytest.raises(RuntimeError):
            create_model("STU-Net-S",
                         pretrained=True,
                         checkpoint_path=os.path.join("tests", "data", "CT_ORG_base_ep1k.model"))

    def test_stunet_s_with_huggingface_checkpoint(self):
        model = create_model(
            "STU-Net-S",
            pretrained=True,
            checkpoint_path="https://huggingface.co/ziyanhuang/STU-Net/blob/main/small_ep4k.model")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])


class TestSTUNet_base():

    def test_stunet_b_simple_example(self):
        model = create_model("STU-Net-B")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_b_with_huggingface_checkpoint(self):
        model = create_model(
            "STU-Net-B",
            pretrained=True,
            checkpoint_path="https://huggingface.co/ziyanhuang/STU-Net/blob/main/base_ep4k.model")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_b_with_huggingface_checkpoint_and_args(self):
        path = "https://huggingface.co/blueyo0/STU-Net_CT-ORG/blob/main/base_ep1k.model"
        model = create_model("STU-Net-B", num_classes=7, pretrained=True, checkpoint_path=path)
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 7, 128, 128, 128])


class TestSTUNet_large():

    def test_stunet_b_simple_example(self):
        model = create_model("STU-Net-L")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_b_with_huggingface_checkpoint(self):
        model = create_model(
            "STU-Net-L",
            pretrained=True,
            checkpoint_path="https://huggingface.co/ziyanhuang/STU-Net/blob/main/large_ep4k.model")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])


class TestSTUNet_huge():

    def test_stunet_h_simple_example(self):
        model = create_model("STU-Net-H")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])

    def test_stunet_h_with_huggingface_checkpoint(self):
        model = create_model(
            "STU-Net-H",
            pretrained=True,
            checkpoint_path="https://huggingface.co/ziyanhuang/STU-Net/blob/main/huge_ep4k.model")
        input_tensor = torch.randn(1, 1, 128, 128, 128)
        output_tensor = model(input_tensor)
        assert output_tensor.shape == torch.Size([1, 105, 128, 128, 128])
