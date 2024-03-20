# home-bots
Robotics at home using the robot operating system ROS2.

Here I experiment with robotics at home to create interesting robots that make life at home easier or generally just more fun.
I plan on first developing robots virtually using Gazebo simulations and later build them in real life.
My plan for this repo is to contain several ros packages for different robots and scenarios as well as some form of documentation of my experiences.

## How to use
This project uses vscode devcontainers to streamline the development process for different developers using different hardware and operating systems. Basically just install [Docker](https://www.docker.com), [VS Code](https://code.visualstudio.com) and the [devcontainers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), clone this project, open in vscode where a message will appear informing you that it found a devcontainer configuration and click on "Reopen in Container". You can find more information on [https://containers.dev](https://containers.dev).

Since I can't get OpenGL programs like rviz to run using this setup on my apple silicon MacBook Air, I use [Foxglove](https://docs.foxglove.dev) for visualizations instead. To connect to the ROS stack in this project, run the foxglove bridge inside the devcontainer:
``` shell
ros2 launch foxglove_bridge foxglove_bridge_launch.xml
```
Then open Foxglove and open a live connection. The default `http://localhost:8765` connection should work fine.