#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Joep Tool
# ---
# MODIFIED FROM: https://github.com/azeey/turtlebot3_simulations/blob/new_gazebo/turtlebot3_gazebo/launch/empty_world.launch.py
# Authors: Joran Schneyer

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    home_bots_gazebo = get_package_share_directory('home_bots_gazebo')
    ros_gz_sim = get_package_share_directory('ros_gz_sim')

    world = os.path.join(home_bots_gazebo, 'worlds', 'empty_world.world')
    set_env_vars_resources = AppendEnvironmentVariable(
        'GZ_SIM_RESOURCE_PATH',
        os.path.join(home_bots_gazebo, 'models')
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': ['-r -s -v4 ', world], 'on_exit_shutdown': 'true'}.items()
    )

    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(set_env_vars_resources)
    ld.add_action(gzserver_cmd)

    return ld