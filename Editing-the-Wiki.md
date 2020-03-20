> [Wiki](Home) >[Editing the Wiki](Editing-the-Wiki)

### Markdown
Markdown is the preferred format for Wiki pages as it supports useful features like code highlighting. Other similar document types are available, for example ReST or MediaWiki may be useful if moving documentation from other sources.

For a 3-minute introduction to Markdown see ['Mastering Markdown'](https://guides.github.com/features/mastering-markdown/).

### Adding Pages

Pages for the Wiki can be created and edited through GitHub or by checking out the Wiki in git and editing locally.

```shell
git clone https://github.com/ISISComputingGroup/ibex_developers_manual.wiki.git
```

Pages can be organised into folders, but only by checking the Wiki out, arranging as desired, and checking everything back in.

### Adding DrawIO Diagram

Create new diagram

1. Visit [DrawIO](https://www.draw.io/) choose `device`
1. Create New Diagram, select type etc.
1. Edit diagram until you are happy
1. choose `File` -> `Export` -> `Png...`
1. Then make sure `Include a copy of my diagram` is ticked
1. Select `github`, then the repo (you may have to show more sources)
1. Type commit comment

In wiki add to markdown using:

    ![alternative text](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/<image name>.png)

To edit this just open that png in `draw.io`.

### Adding Images

To add images you need to check out the Wiki and add them manually. The images should go in their own folder, for example, an image for this page would need to go in `/images/using_the_wiki/`.

```shell
git add images/using_the_wiki/test.png
git commit -m "Added an image to Using the Wiki page"
git push
```

You can then add the image in markdown using the URL `images/using_the_wiki/test.png`:

    ![alternative text](https://raw.githubusercontent.com/ISISComputingGroup/ibex_developers_manual/master/images/using_the_wiki/test.png)

### Adding or Editing Files

To add or edit a file you again need to check out the Wiki and add manually, or edit and push existing documents. Documents should be stored with their associated pages.

### Adding breadcrumb trails

The Wiki is largely unstructured. To help provide navigation breadcrumb trails can be used. Insert the following at the top of the page:

```
> [Wiki](Home) ▸ [[Level 1]] ▸ [[Level 2]] ▸ **Document Title**
```

