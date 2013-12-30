SublimeLinter-apiblueprint
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [ApiBlueprint](https://github.com/apiaryio/api-blueprint) via [Snow Crash](https://github.com/apiaryio/snowcrash). It will be used with files that have the “ApiBlueprint” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Installation).

### Linter installation
Before using this plugin, you must ensure that `Snow Crash` is installed on your system. To install `Snow Crash`, check [the homepage](https://github.com/apiaryio/snowcrash), or do the following:

#### OS X

```sh
$ brew install --HEAD \
  https://raw.github.com/apiaryio/snowcrash/master/tools/homebrew/snowcrash.rb
```

#### Windows

See [this page](https://github.com/apiaryio/snowcrash/wiki/Building-on-Windows)

#### Other Systems

See [this page](https://github.com/apiaryio/snowcrash#build)

Once apiblueprint is installed, you can proceed to install the SublimeLinter-apiblueprint plugin if it is not yet installed.

### Plugin installation

#### From the source

```sh
$ cd '/path/to/Sublime Text 3/Packages'
$ git clone https://github.com/SublimeLinter/SublimeLinter3.git SublimeLinter
$ git clone https://github.com/WMeldon/SublimeLinter-apiblueprint.git "SublimeLinter - API Blueprint"
```

#### Using Package Control
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `apiblueprint`. Among the entries you should see `SublimeLinter-apiblueprint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings). For information on generic linter settings, please see [Linter Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
