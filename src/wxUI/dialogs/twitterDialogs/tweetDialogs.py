""" GUI dialogs for tweet writing and displaying. """
import wx
from typing import List

class tweet(wx.Dialog):
    def __init__(self, title: str, caption: str, message: str = "", max_length: int = 280, thread_mode: bool = True, *args, **kwds) -> None:
        """ Creates the basic Tweet dialog. This might be considered the base class for other dialogs.
        title str: title to be used in the dialog.
        caption str: This is the text to be placed alongside the text field.
        message str: Text to be inserted in the tweet.
        max_length int: Maximum amount of characters the tweet will accept. By default is 280 chahracters.
        thread_mode bool: If set to False, disables the button that allows to make threads by adding more tweets.
        """
        super(tweet, self).__init__(parent=None, *args, **kwds)
        self.SetTitle(title)
        self.create_controls(max_length=max_length, caption=caption, message=message, thread_mode=thread_mode)

    def create_controls(self, message: str, caption: str, max_length: int, thread_mode: bool) -> None:
        panel = wx.Panel(self)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(text_sizer, 1, wx.EXPAND, 0)
        label_1 = wx.StaticText(panel, wx.ID_ANY, caption)
        text_sizer.Add(label_1, 0, 0, 0)
        self.text = wx.TextCtrl(panel, wx.ID_ANY, "", size=(444, -1), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_CHAR_HOOK, self.handle_keys, self.text)
        text_sizer.Add(self.text, 1, wx.EXPAND, 0)
        list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(list_sizer, 1, wx.EXPAND, 0)
        Attachment_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(Attachment_sizer, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(panel, wx.ID_ANY, _("Attachments"))
        Attachment_sizer.Add(label_2, 0, 0, 0)
        self.attachments = wx.ListCtrl(panel, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.attachments.AppendColumn(_("File"))
        self.attachments.AppendColumn(_("Type"))
        self.attachments.AppendColumn(_("Description"))
        Attachment_sizer.Add(self.attachments, 1, wx.EXPAND, 0)
        self.remove_attachment = wx.Button(panel, wx.ID_ANY, _("Delete attachment"))
        self.remove_attachment.Enable(False)
        Attachment_sizer.Add(self.remove_attachment, 0, 0, 0)
        tweet_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(tweet_sizer, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(panel, wx.ID_ANY, _("Added Tweets"))
        tweet_sizer.Add(label_3, 0, 0, 0)
        self.tweets = wx.ListCtrl(panel, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.tweets.AppendColumn(_("Text"))
        self.tweets.AppendColumn(_("Attachments"))
        self.tweets.Enable(False)
        tweet_sizer.Add(self.tweets, 1, wx.EXPAND, 0)
        self.remove_tweet = wx.Button(panel, wx.ID_ANY, _("Delete tweet"))
        self.remove_tweet.Enable(False)
        tweet_sizer.Add(self.remove_tweet, 0, 0, 0)
        btn_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_1, 1, wx.EXPAND, 0)
        self.add = wx.Button(panel, wx.ID_ANY, _("A&dd..."))
        btn_sizer_1.Add(self.add, 0, 0, 0)
        self.add_tweet = wx.Button(panel, wx.ID_ANY, _("Add t&weet"))
        self.add_tweet.Enable(thread_mode)
        btn_sizer_1.Add(self.add_tweet, 0, 0, 0)
        self.add_audio = wx.Button(panel, wx.ID_ANY, _("&Attach audio..."))
        btn_sizer_1.Add(self.add_audio, 0, 0, 0)
        btn_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_2, 1, wx.EXPAND, 0)
        self.autocomplete_users = wx.Button(panel, wx.ID_ANY, _("Auto&complete users"))
        btn_sizer_2.Add(self.autocomplete_users, 0, 0, 0)
        self.spellcheck = wx.Button(panel, wx.ID_ANY, _("Check &spelling..."))
        btn_sizer_2.Add(self.spellcheck, 0, 0, 0)
        self.translate = wx.Button(panel, wx.ID_ANY, _("&Translate"))
        btn_sizer_2.Add(self.translate, 0, 0, 0)
        ok_cancel_sizer = wx.StdDialogButtonSizer()
        mainBox.Add(ok_cancel_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.send = wx.Button(panel, wx.ID_OK, _("Sen&d"))
        self.send.SetDefault()
        ok_cancel_sizer.Add(self.send, 0, 0, 0)
        self.cancel = wx.Button(panel, wx.ID_CANCEL, "")
        ok_cancel_sizer.AddButton(self.cancel)
        ok_cancel_sizer.Realize()
        panel.SetSizer(mainBox)
        self.Fit()
        self.SetAffirmativeId(self.send.GetId())
        self.SetEscapeId(self.cancel.GetId())
        self.Layout()

    def handle_keys(self, event: wx.Event, *args, **kwargs) -> None:
        """ Allows to react to certain keyboard events from the text control. """
        shift=event.ShiftDown()
        if event.GetKeyCode() == wx.WXK_RETURN and shift==False and hasattr(self,'send'):
            self.EndModal(wx.ID_OK)
        else:
            event.Skip()

    def reset_controls(self) -> None:
        """ Resetss text control and attachments to their default, empty values. This is used while adding more tweets in a  thread. """
        self.text.ChangeValue("")
        self.attachments.DeleteAllItems()

    def add_item(self, list_type: str = "attachment", item: List[str] = []) -> None:
        """ Adds an item to a list control. Item should be a list with the same amount of items for each column present in the ListCtrl. """
        if list_type == "attachment":
            self.attachments.Append(item)
        else:
            self.tweets.Append(item)

    def remove_item(self, list_type: str = "attachment") -> None:
        if list_type == "attachment":
            item = self.attachments.GetFocusedItem()
            if item > -1:
                self.attachments.DeleteItem(item)
        else:
            item = self.tweets.GetFocusedItem()
            if item > -1:
                self.tweets.DeleteItem(item)

    def attach_menu(self, event=None, enabled=True, *args, **kwargs):
        menu = wx.Menu()
        self.add_image = menu.Append(wx.ID_ANY, _("Image"))
        self.add_image.Enable(enabled)
        self.add_video = menu.Append(wx.ID_ANY, _("Video"))
        self.add_video.Enable(enabled)
        self.add_poll = menu.Append(wx.ID_ANY, _("Poll"))
        self.add_poll.Enable(enabled)
        return menu

    def ask_description(self):
        dlg = wx.TextEntryDialog(self, _(u"please provide a description"), _(u"Description"))
        dlg.ShowModal()
        result = dlg.GetValue()
        dlg.Destroy()
        return result

    def get_image(self):
        openFileDialog = wx.FileDialog(self, _(u"Select the picture to be uploaded"), "", "", _("Image files (*.png, *.jpg, *.gif)|*.png; *.jpg; *.gif"), wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return (None, None)
        dsc = self.ask_description()
        return (openFileDialog.GetPath(), dsc)

    def get_video(self):
        openFileDialog = wx.FileDialog(self, _("Select the video to be uploaded"), "", "", _("Video files (*.mp4)|*.mp4"), wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return None
        return openFileDialog.GetPath()

    def unable_to_attach_file(self, *args, **kwargs):
        return wx.MessageDialog(self, _("It is not possible to add more attachments. Please make sure your tweet complies with Twitter'S attachment rules. You can add only one video or GIF in every tweet, and a maximum of 4 photos."), _("Error adding attachment"), wx.ICON_ERROR).ShowModal()

class reply(tweet):

    def __init__(self, users: List[str] = [], *args, **kwargs) -> None:
        self.users = users
        super(reply, self).__init__(*args, **kwargs)

    def create_controls(self, message: str, caption: str, max_length: int, thread_mode: bool) -> None:
        panel = wx.Panel(self)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(text_sizer, 1, wx.EXPAND, 0)
        label_1 = wx.StaticText(panel, wx.ID_ANY, caption)
        text_sizer.Add(label_1, 0, 0, 0)
        self.text = wx.TextCtrl(panel, wx.ID_ANY, "", size=(500, 200), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_CHAR_HOOK, self.handle_keys, self.text)
        text_sizer.Add(self.text, 1, wx.EXPAND, 0)
        list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(list_sizer, 1, wx.EXPAND, 0)
        Attachment_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(Attachment_sizer, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(panel, wx.ID_ANY, _("Attachments"))
        Attachment_sizer.Add(label_2, 0, 0, 0)
        self.attachments = wx.ListCtrl(panel, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.attachments.AppendColumn(_("File"))
        self.attachments.AppendColumn(_("Type"))
        self.attachments.AppendColumn(_("Description"))
        Attachment_sizer.Add(self.attachments, 1, wx.EXPAND, 0)
        self.remove_attachment = wx.Button(panel, wx.ID_ANY, _("Delete attachment"))
        self.remove_attachment.Enable(False)
        Attachment_sizer.Add(self.remove_attachment, 0, 0, 0)
        user_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(user_sizer, 0, 0, 0)
        self.mention_all = wx.CheckBox(panel, -1, _(u"&Mention to all"), size=wx.DefaultSize)
        self.mention_all.Disable()
        user_sizer.Add(self.mention_all, 0, wx.ALL, 5)
        self.checkboxes = []
        for i in self.users:
            user_checkbox = wx.CheckBox(panel, -1, "@"+i, size=wx.DefaultSize)
            self.checkboxes.append(user_checkbox)
            user_sizer.Add(self.checkboxes[-1], 0, wx.ALL, 5)
        btn_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_1, 1, wx.EXPAND, 0)
        self.add = wx.Button(panel, wx.ID_ANY, _("A&dd..."))
        btn_sizer_1.Add(self.add, 0, 0, 0)
        self.add_audio = wx.Button(panel, wx.ID_ANY, _("&Attach audio..."))
        btn_sizer_1.Add(self.add_audio, 0, 0, 0)
        btn_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_2, 1, wx.EXPAND, 0)
        self.autocomplete_users = wx.Button(panel, wx.ID_ANY, _("Auto&complete users"))
        btn_sizer_2.Add(self.autocomplete_users, 0, 0, 0)
        self.spellcheck = wx.Button(panel, wx.ID_ANY, _("Check &spelling..."))
        btn_sizer_2.Add(self.spellcheck, 0, 0, 0)
        self.translate = wx.Button(panel, wx.ID_ANY, _("&Translate"))
        btn_sizer_2.Add(self.translate, 0, 0, 0)
        ok_cancel_sizer = wx.StdDialogButtonSizer()
        mainBox.Add(ok_cancel_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.send = wx.Button(panel, wx.ID_OK, _("Sen&d"))
        self.send.SetDefault()
        ok_cancel_sizer.Add(self.send, 0, 0, 0)
        self.cancel = wx.Button(panel, wx.ID_CANCEL, "")
        ok_cancel_sizer.AddButton(self.cancel)
        ok_cancel_sizer.Realize()
        panel.SetSizer(mainBox)
        self.Fit()
        self.SetAffirmativeId(self.send.GetId())
        self.SetEscapeId(self.cancel.GetId())
        self.Layout()

    def attach_menu(self, event=None, enabled=True, *args, **kwargs):
        menu = wx.Menu()
        self.add_image = menu.Append(wx.ID_ANY, _("Image"))
        self.add_image.Enable(enabled)
        self.add_video = menu.Append(wx.ID_ANY, _("Video"))
        self.add_video.Enable(enabled)
        return menu

class dm(tweet):

    def __init__(self, users: List[str] = [], *args, **kwargs) -> None:
        self.users = users
        super(dm, self).__init__(*args, **kwargs)

    def create_controls(self, message: str, caption: str, max_length: int, thread_mode: bool) -> None:
        panel = wx.Panel(self)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        label_recipient = wx.StaticText(panel, -1, _("&Recipient"))
        self.cb = wx.ComboBox(panel, -1, choices=self.users, value=self.users[0], size=wx.DefaultSize)
        self.autocomplete_users = wx.Button(panel, -1, _(u"Auto&complete users"))
        recipient_sizer = wx.BoxSizer(wx.HORIZONTAL)
        recipient_sizer.Add(label_recipient, 0, 0, 0)
        recipient_sizer.Add(self.cb, 1, wx.EXPAND, 0)
        mainBox.Add(recipient_sizer, 0, wx.EXPAND, 0)
        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(text_sizer, 1, wx.EXPAND, 0)
        label_1 = wx.StaticText(panel, wx.ID_ANY, caption)
        text_sizer.Add(label_1, 0, 0, 0)
        self.text = wx.TextCtrl(panel, wx.ID_ANY, "", size=(500, 200), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_CHAR_HOOK, self.handle_keys, self.text)
        self.text.SetFocus()
        text_sizer.Add(self.text, 1, wx.EXPAND, 0)
        list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(list_sizer, 1, wx.EXPAND, 0)
        Attachment_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(Attachment_sizer, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(panel, wx.ID_ANY, _("Attachments"))
        Attachment_sizer.Add(label_2, 0, 0, 0)
        self.attachments = wx.ListCtrl(panel, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.attachments.AppendColumn(_("File"))
        self.attachments.AppendColumn(_("Type"))
        self.attachments.AppendColumn(_("Description"))
        Attachment_sizer.Add(self.attachments, 1, wx.EXPAND, 0)
        self.remove_attachment = wx.Button(panel, wx.ID_ANY, _("Delete attachment"))
        self.remove_attachment.Enable(False)
        Attachment_sizer.Add(self.remove_attachment, 0, 0, 0)
        btn_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_1, 1, wx.EXPAND, 0)
        self.add = wx.Button(panel, wx.ID_ANY, _("A&dd..."))
        btn_sizer_1.Add(self.add, 0, 0, 0)
        self.add_audio = wx.Button(panel, wx.ID_ANY, _("&Attach audio..."))
        btn_sizer_1.Add(self.add_audio, 0, 0, 0)
        btn_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        mainBox.Add(btn_sizer_2, 1, wx.EXPAND, 0)
        self.spellcheck = wx.Button(panel, wx.ID_ANY, _("Check &spelling..."))
        btn_sizer_2.Add(self.spellcheck, 0, 0, 0)
        self.translate = wx.Button(panel, wx.ID_ANY, _("&Translate"))
        btn_sizer_2.Add(self.translate, 0, 0, 0)
        ok_cancel_sizer = wx.StdDialogButtonSizer()
        mainBox.Add(ok_cancel_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.send = wx.Button(panel, wx.ID_OK, _("Sen&d"))
        self.send.SetDefault()
        ok_cancel_sizer.Add(self.send, 0, 0, 0)
        self.cancel = wx.Button(panel, wx.ID_CANCEL, "")
        ok_cancel_sizer.AddButton(self.cancel)
        ok_cancel_sizer.Realize()
        panel.SetSizer(mainBox)
        self.Fit()
        self.SetAffirmativeId(self.send.GetId())
        self.SetEscapeId(self.cancel.GetId())
        self.Layout()

    def get_image(self):
        openFileDialog = wx.FileDialog(self, _(u"Select the picture to be uploaded"), "", "", _("Image files (*.png, *.jpg, *.gif)|*.png; *.jpg; *.gif"), wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return (None, None)
        return (openFileDialog.GetPath(), "")

    def attach_menu(self, event=None, enabled=True, *args, **kwargs):
        menu = wx.Menu()
        self.add_image = menu.Append(wx.ID_ANY, _("Image"))
        self.add_image.Enable(enabled)
        self.add_video = menu.Append(wx.ID_ANY, _("Video"))
        self.add_video.Enable(enabled)
        return menu

class viewTweet(wx.Dialog):
    def set_title(self, lenght):
        self.SetTitle(_(u"Tweet - %i characters ") % (lenght,))

    def __init__(self, text, rt_count, favs_count, source, date="", *args, **kwargs):
        super(viewTweet, self).__init__(None, size=(850,850))
        panel = wx.Panel(self)
        label = wx.StaticText(panel, -1, _(u"Tweet"))
        self.text = wx.TextCtrl(panel, -1, text, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(250, 180))
        dc = wx.WindowDC(self.text)
        dc.SetFont(self.text.GetFont())
        (x, y) = dc.GetMultiLineTextExtent("W"*280)
        self.text.SetSize((x, y))
        self.text.SetFocus()
        textBox = wx.BoxSizer(wx.HORIZONTAL)
        textBox.Add(label, 0, wx.ALL, 5)
        textBox.Add(self.text, 1, wx.EXPAND, 5)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(textBox, 0, wx.ALL, 5)
        label2 = wx.StaticText(panel, -1, _(u"Image description"))
        self.image_description = wx.TextCtrl(panel, -1, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(250, 180))
        dc = wx.WindowDC(self.image_description)
        dc.SetFont(self.image_description.GetFont())
        (x, y) = dc.GetMultiLineTextExtent("0"*450)
        self.image_description.SetSize((x, y))
        self.image_description.Enable(False)
        iBox = wx.BoxSizer(wx.HORIZONTAL)
        iBox.Add(label2, 0, wx.ALL, 5)
        iBox.Add(self.image_description, 1, wx.EXPAND, 5)
        mainBox.Add(iBox, 0, wx.ALL, 5)
        rtCountLabel = wx.StaticText(panel, -1, _(u"Retweets: "))
        rtCount = wx.TextCtrl(panel, -1, rt_count, size=wx.DefaultSize, style=wx.TE_READONLY|wx.TE_MULTILINE)
        rtBox = wx.BoxSizer(wx.HORIZONTAL)
        rtBox.Add(rtCountLabel, 0, wx.ALL, 5)
        rtBox.Add(rtCount, 0, wx.ALL, 5)
        favsCountLabel = wx.StaticText(panel, -1, _(u"Likes: "))
        favsCount = wx.TextCtrl(panel, -1, favs_count, size=wx.DefaultSize, style=wx.TE_READONLY|wx.TE_MULTILINE)
        favsBox = wx.BoxSizer(wx.HORIZONTAL)
        favsBox.Add(favsCountLabel, 0, wx.ALL, 5)
        favsBox.Add(favsCount, 0, wx.ALL, 5)
        sourceLabel = wx.StaticText(panel, -1, _(u"Source: "))
        sourceTweet = wx.TextCtrl(panel, -1, source, size=wx.DefaultSize, style=wx.TE_READONLY|wx.TE_MULTILINE)
        sourceBox = wx.BoxSizer(wx.HORIZONTAL)
        sourceBox.Add(sourceLabel, 0, wx.ALL, 5)
        sourceBox.Add(sourceTweet, 0, wx.ALL, 5)
        dateLabel = wx.StaticText(panel, -1, _(u"Date: "))
        dateTweet = wx.TextCtrl(panel, -1, date, size=wx.DefaultSize, style=wx.TE_READONLY|wx.TE_MULTILINE)
        dc = wx.WindowDC(dateTweet)
        dc.SetFont(dateTweet.GetFont())
        (x, y) = dc.GetTextExtent("0"*100)
        dateTweet.SetSize((x, y))
        dateBox = wx.BoxSizer(wx.HORIZONTAL)
        dateBox.Add(dateLabel, 0, wx.ALL, 5)
        dateBox.Add(dateTweet, 0, wx.ALL, 5)
        infoBox = wx.BoxSizer(wx.HORIZONTAL)
        infoBox.Add(rtBox, 0, wx.ALL, 5)
        infoBox.Add(favsBox, 0, wx.ALL, 5)
        infoBox.Add(sourceBox, 0, wx.ALL, 5)
        mainBox.Add(infoBox, 0, wx.ALL, 5)
        mainBox.Add(dateBox, 0, wx.ALL, 5)
        self.share = wx.Button(panel, wx.ID_ANY, _("Copy link to clipboard"))
        self.share.Enable(False)
        self.spellcheck = wx.Button(panel, -1, _("Check &spelling..."), size=wx.DefaultSize)
        self.translateButton = wx.Button(panel, -1, _(u"&Translate..."), size=wx.DefaultSize)
        cancelButton = wx.Button(panel, wx.ID_CANCEL, _(u"C&lose"), size=wx.DefaultSize)
        cancelButton.SetDefault()
        buttonsBox = wx.BoxSizer(wx.HORIZONTAL)
        buttonsBox.Add(self.share, 0, wx.ALL, 5)
        buttonsBox.Add(self.spellcheck, 0, wx.ALL, 5)
        buttonsBox.Add(self.translateButton, 0, wx.ALL, 5)
        buttonsBox.Add(cancelButton, 0, wx.ALL, 5)
        mainBox.Add(buttonsBox, 0, wx.ALL, 5)
        selectId = wx.ID_ANY
        self.Bind(wx.EVT_MENU, self.onSelect, id=selectId)
        self.accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL, ord('A'), selectId),
        ])
        self.SetAcceleratorTable(self.accel_tbl)
        panel.SetSizer(mainBox)
        self.SetClientSize(mainBox.CalcMin())

    def set_text(self, text):
        self.text.ChangeValue(text)

    def get_text(self):
        return self.text.GetValue()

    def set_image_description(self, desc):
        self.image_description.Enable(True)
        if len(self.image_description.GetValue()) == 0:
            self.image_description.SetValue(desc)
        else:
            self.image_description.SetValue(self.image_description.GetValue()+"\n"+desc)

    def text_focus(self):
        self.text.SetFocus()

    def onSelect(self, ev):
        self.text.SelectAll()

    def enable_button(self, buttonName):
        if hasattr(self, buttonName):
            return getattr(self, buttonName).Enable()

class viewNonTweet(wx.Dialog):

    def __init__(self, text, date="", *args, **kwargs):
        super(viewNonTweet, self).__init__(None, size=(850,850))
        self.SetTitle(_(u"View"))
        panel = wx.Panel(self)
        label = wx.StaticText(panel, -1, _(u"Item"))
        self.text = wx.TextCtrl(parent=panel, id=-1, value=text, style=wx.TE_READONLY|wx.TE_MULTILINE, size=(250, 180))
        dc = wx.WindowDC(self.text)
        dc.SetFont(self.text.GetFont())
        (x, y) = dc.GetMultiLineTextExtent("0"*140)
        self.text.SetSize((x, y))
        self.text.SetFocus()
        textBox = wx.BoxSizer(wx.HORIZONTAL)
        textBox.Add(label, 0, wx.ALL, 5)
        textBox.Add(self.text, 1, wx.EXPAND, 5)
        mainBox = wx.BoxSizer(wx.VERTICAL)
        mainBox.Add(textBox, 0, wx.ALL, 5)
        if date != "":
            dateLabel = wx.StaticText(panel, -1, _(u"Date: "))
            date = wx.TextCtrl(panel, -1, date, size=wx.DefaultSize, style=wx.TE_READONLY|wx.TE_MULTILINE)
            dc = wx.WindowDC(date)
            dc.SetFont(date.GetFont())
            (x, y) = dc.GetTextExtent("0"*100)
            date.SetSize((x, y))
            dateBox = wx.BoxSizer(wx.HORIZONTAL)
            dateBox.Add(dateLabel, 0, wx.ALL, 5)
            dateBox.Add(date, 0, wx.ALL, 5)
            mainBox.Add(dateBox, 0, wx.ALL, 5)
        self.share = wx.Button(panel, wx.ID_ANY, _("Copy link to clipboard"))
        self.share.Enable(False)
        self.spellcheck = wx.Button(panel, -1, _("Check &spelling..."), size=wx.DefaultSize)
        self.unshortenButton = wx.Button(panel, -1, _(u"&Expand URL"), size=wx.DefaultSize)
        self.unshortenButton.Disable()
        self.translateButton = wx.Button(panel, -1, _(u"&Translate..."), size=wx.DefaultSize)
        cancelButton = wx.Button(panel, wx.ID_CANCEL, _(u"C&lose"), size=wx.DefaultSize)
        cancelButton.SetDefault()
        buttonsBox = wx.BoxSizer(wx.HORIZONTAL)
        buttonsBox.Add(self.share, 0, wx.ALL, 5)
        buttonsBox.Add(self.spellcheck, 0, wx.ALL, 5)
        buttonsBox.Add(self.unshortenButton, 0, wx.ALL, 5)
        buttonsBox.Add(self.translateButton, 0, wx.ALL, 5)
        buttonsBox.Add(cancelButton, 0, wx.ALL, 5)
        mainBox.Add(buttonsBox, 0, wx.ALL, 5)
        selectId = wx.ID_ANY
        self.Bind(wx.EVT_MENU, self.onSelect, id=selectId)
        self.accel_tbl = wx.AcceleratorTable([
            (wx.ACCEL_CTRL, ord('A'), selectId),
        ])
        self.SetAcceleratorTable(self.accel_tbl)
        panel.SetSizer(mainBox)
        self.SetClientSize(mainBox.CalcMin())

    def onSelect(self, ev):
        self.text.SelectAll()

    def set_text(self, text):
        self.text.ChangeValue(text)

    def get_text(self):
        return self.text.GetValue()

    def text_focus(self):
        self.text.SetFocus()

    def enable_button(self, buttonName):
        if hasattr(self, buttonName):
            return getattr(self, buttonName).Enable()

class poll(wx.Dialog):
    def __init__(self, *args, **kwds):
        super(poll, self).__init__(parent=None, id=wx.NewId(), title=_("Add a poll"))
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        period_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(period_sizer, 1, wx.EXPAND, 0)
        label_period = wx.StaticText(self, wx.ID_ANY, _("Participation time (in days)"))
        period_sizer.Add(label_period, 0, 0, 0)
        self.period = wx.SpinCtrl(self, wx.ID_ANY)
        self.period.SetFocus()
        self.period.SetRange(1, 7)
        self.period.SetValue(7)
        period_sizer.Add(self.period, 0, 0, 0)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, _("Choices")), wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        option1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(option1_sizer, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, _("Option 1"))
        option1_sizer.Add(label_2, 0, 0, 0)
        self.option1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.option1.SetMaxLength(25)
        option1_sizer.Add(self.option1, 0, 0, 0)
        option2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(option2_sizer, 1, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, _("Option 2"))
        option2_sizer.Add(label_3, 0, 0, 0)
        self.option2 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.option2.SetMaxLength(25)
        option2_sizer.Add(self.option2, 0, 0, 0)
        option3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(option3_sizer, 1, wx.EXPAND, 0)
        label_4 = wx.StaticText(self, wx.ID_ANY, _("Option 3"))
        option3_sizer.Add(label_4, 0, 0, 0)
        self.option3 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.option3.SetMaxLength(25)
        option3_sizer.Add(self.option3, 0, 0, 0)
        option4_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(option4_sizer, 1, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, _("Option 4"))
        option4_sizer.Add(label_5, 0, 0, 0)
        self.option4 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.option4.SetMaxLength(25)
        option4_sizer.Add(self.option4, 0, 0, 0)
        btn_sizer = wx.StdDialogButtonSizer()
        sizer_1.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)
        self.button_OK = wx.Button(self, wx.ID_OK)
        self.button_OK.SetDefault()
        self.button_OK.Bind(wx.EVT_BUTTON, self.validate_data)
        btn_sizer.AddButton(self.button_OK)
        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        btn_sizer.AddButton(self.button_CANCEL)
        btn_sizer.Realize()
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())
        self.Layout()

    def get_options(self):
        controls = [self.option1, self.option2, self.option3, self.option4]
        options = [option.GetValue() for option in controls if option.GetValue() != ""]
        return options

    def validate_data(self, *args, **kwargs):
        options = self.get_options()
        if len(options) < 2:
            return wx.MessageDialog(self, _("Please make sure you have provided at least two options for the poll."), _("Not enough information"), wx.ICON_ERROR).ShowModal()
        self.EndModal(wx.ID_OK)