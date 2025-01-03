from transformers import AutoModel

import torch
import logging
import os
from copy import deepcopy

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/log.log",
    level=logging.DEBUG,
    format="[%(asctime)s | %(funcName)s @ %(pathname)s] %(message)s",
)
logger = logging.getLogger()


class BiEncoder(torch.nn.Module):
    def __init__(self):
        super(BiEncoder, self).__init__()
        self.passage_encoder = AutoModel.from_pretrained("klue/bert-base")
        self.query_encoder = AutoModel.from_pretrained("klue/bert-base")
        self.emb_sz = (
            self.passage_encoder.pooler.dense.out_features
        )  # get cls token dim

    def forward(
        self, x: torch.LongTensor, attn_mask: torch.LongTensor, type: str = "passage"
    ) -> torch.FloatTensor:
        """passage 또는 query를 bert로 encoding합니다."""
        assert type in (
            "passage",
            "query",
        ), "type should be either 'passage' or 'query'"
        if type == "passage":
            return self.passage_encoder(
                input_ids=x, attention_mask=attn_mask
            ).pooler_output
        else:
            return self.query_encoder(
                input_ids=x, attention_mask=attn_mask
            ).pooler_output

    def checkpoint(self, model_ckpt_path):
        """state dict를 저장한다."""
        torch.save(deepcopy(self.state_dict()), model_ckpt_path)
        logger.debug(f"model self.state_dict saved to {model_ckpt_path}")

    def load(self, model_ckpt_path, device=None):
        with open(model_ckpt_path, "rb") as f:
            state_dict = torch.load(f, map_location=device)
        self.load_state_dict(state_dict)
        logger.debug(f"model self.state_dict loaded from {model_ckpt_path}")
