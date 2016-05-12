### Markdown
Markdown is the preferred format for Wiki pages as it supports useful features like code highlighting. Other similar document types are available, for example ReST or MediaWiki may be useful if moving documentation from other sources.

For a 3-minute introduction to Markdown see ['Mastering Markdown'](https://guides.github.com/features/mastering-markdown/).

### Adding Pages

Pages for the Wiki can be created and edited through GitHub or by checking out the Wiki in git and editing locally.

```shell
git clone https://github.com/ISISComputingGroup/ibex_developers_manual.wiki.git
```

Pages can be organised into folders, but only by checking the Wiki out, arranging as desired, and checking everything back in.

### Adding Images

To add images you need to check out the Wiki and add them manually. The images should go in their own folder, for example an image for this page would need to go in `/images/using_the_wiki/`.

```shell
git add images/using_the_wiki/test.png
git commit -m "Added an image to Using the Wiki page"
git push
```

### Adding breadcrumb trails

The Wiki is largely unstrctured. To help provide navigation breadcrumb trails can be used. Insert the following at the top of the page:

```
> [Wiki](Home) ▸ [[Level 1]] ▸ [[Level 2]] ▸ **Document Title**
```

