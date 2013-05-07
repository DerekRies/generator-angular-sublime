## Generator-Angular-Sublime

This is a Sublime Text 2 plugin that supports the features provided by the generator-angular yeoman generator. Instead of having to tab out of sublime, open up a terminal, then enter in exhaustingly long "yo angular:route myroute", then tab back into sublime, and finally open up the files that were created; just open up the command palette, type route, enter a name, and let the plugin do the rest.

This is just something I hacked together because I was getting a little fatigued by the experience described above. It only supports the scaffolding commands once the app has already been created at the moment. Should have the ability to create new angular apps from sublime soon as well.

### Usage

At the moment the plugin expects your project to be the first folder in your sidebar, this is the folder that generator-angular will be manipulating.

Bring up your command palette and begin typing Yeoman, you should see a list of all the generator angular commands, choose one to run it and fill out the information you're prompted for. You should have your newly created files opened for you.