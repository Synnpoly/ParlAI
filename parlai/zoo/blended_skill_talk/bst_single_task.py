#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Pretrained polyencoder retrieval model on the BlendedSkillTalk dialogue task.
"""

from parlai.core.build_data import download_models


def download(datapath):
    model_type = 'bst_single_task'
    version = 'v1.0'
    opt = {'datapath': datapath, 'model_type': model_type}
    fnames = ['model', 'model.dict', 'model.dict.codecs', 'model.dict.opt', 'model.opt']
    download_models(
        opt=opt,
        fnames=fnames,
        model_folder='blended_skill_talk',
        version=version,
        path=f'http://localhost:8000/blended_skill_talk/{model_type}',
        use_model_type=True,
    )
    # TODO: remove `path` arg