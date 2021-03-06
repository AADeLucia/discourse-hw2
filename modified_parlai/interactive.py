#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Basic script which allows local human keyboard input to talk to a trained model.

Examples
--------

.. code-block:: shell

  python examples/interactive.py -m drqa -mf "models:drqa/squad/model"

When prompted, enter something like: ``Bob is Blue.\\nWhat is Bob?``

Input is often model or task specific, but in drqa, it is always
``context '\\n' question``.
"""
from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.agents.local_human.local_human import LocalHumanAgent
from parlai.utils.world_logging import WorldLogger

import random


def setup_args(parser=None):
    if parser is None:
        parser = ParlaiParser(True, True, 'Interactive chat with a model')
    parser.add_argument('-d', '--display-examples', type='bool', default=False)
    parser.add_argument(
        '--display-prettify',
        type='bool',
        default=False,
        help='Set to use a prettytable when displaying '
        'examples with text candidates',
    )
    parser.add_argument(
        '--display-ignore-fields',
        type=str,
        default='label_candidates,text_candidates',
        help='Do not display these fields',
    )
    parser.add_argument(
        '-it',
        '--interactive-task',
        type='bool',
        default=True,
        help='Create interactive version of task',
    )
    parser.add_argument(
        '-rf',
        '--report-filename',
        type=str,
        default='',
        help='Saves a json file of the evaluation report either as an '
        'extension to the model-file (if begins with a ".") or a whole '
        'file path. Set to the empty string to not save at all.',
    )
    parser.add_argument(
        '--save-world-logs',
        type='bool',
        default=False,
        help='Saves a jsonl file containing all of the task examples and '
        'model replies. Must also specify --report-filename.',
    )
    parser.add_argument(
        '--world-logs-format',
        type=str,
        default='parlai',
        choices=['jsonl', 'parlai', 'forever'],
        help='File format to save chat logs. (default parlai)'
    )
    parser.add_argument('-ltim', '--log-every-n-secs', type=float, default=2)
    parser.set_defaults(interactive_mode=True, task='interactive')
    LocalHumanAgent.add_cmdline_args(parser)
    WorldLogger.add_cmdline_args(parser)
    return parser


def interactive(opt, print_parser=None):
    if print_parser is not None:
        if print_parser is True and isinstance(opt, ParlaiParser):
            print_parser = opt
        elif print_parser is False:
            print_parser = None
    if isinstance(opt, ParlaiParser):
        print('[ Deprecated Warning: interactive should be passed opt not Parser ]')
        opt = opt.parse_args()

    # Create model and assign it to the specified task
    agent = create_agent(opt, requireModelExists=True)
    human_agent = LocalHumanAgent(opt)
    world = create_task(opt, [human_agent, agent])
    # set up world logger
    world_logger = WorldLogger(opt) if opt['save_world_logs'] else None

    if print_parser:
        # Show arguments after loading model
        print_parser.opt = agent.opt
        print_parser.print_args()

    # Show some example dialogs:
    while True:
        try:
            world.parley()
            if world_logger is not None:
                world_logger.log(world)
            if opt.get('display_examples'):
                print("---")
                print(world.display())
            if world.epoch_done():
                print("EPOCH DONE")
                break
        except KeyboardInterrupt:
            if world_logger is not None:
                print(f"\nWriting out world log.")
                # Save report
                report = world.report()
                world.reset()

                # dump world acts to file
                world_logger.reset()  # add final acts to logs
                base_outfile = opt['report_filename'].split('.')[0]
                outfile = base_outfile + f'_interactive_replies.json'
                world_logger.write(outfile, file_format=opt['world_logs_format'])
            quit()


if __name__ == '__main__':
    random.seed(42)
    parser = setup_args()
    interactive(parser.parse_args(print_args=False), print_parser=parser)
