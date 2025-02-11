# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
import application

def retweet_as_link(parent):
    return wx.MessageDialog(parent, _(u"This retweet is over 140 characters. Would you like to post it as a mention to the poster with your comments and a link to the original tweet?"), application.name, wx.YES_NO|wx.ICON_QUESTION).ShowModal()

def retweet_question(parent):
    return wx.MessageDialog(parent, _(u"Would you like to add a comment to this tweet?"), _("Retweet"), wx.YES_NO|wx.CANCEL|wx.ICON_QUESTION).ShowModal()

def delete_tweet_dialog(parent):
    return wx.MessageDialog(parent, _(u"Do you really want to delete this tweet? It will be deleted from Twitter as well."), _(u"Delete"), wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def exit_dialog(parent):
    dlg = wx.MessageDialog(parent, _(u"Do you really want to close {0}?").format(application.name,), _(u"Exit"), wx.YES_NO|wx.ICON_QUESTION)
    return dlg.ShowModal()

def needs_restart():
    wx.MessageDialog(None, _(u" {0} must be restarted for these changes to take effect.").format(application.name,), _("Restart {0} ").format(application.name,), wx.OK).ShowModal()

def delete_user_from_db():
    return wx.MessageDialog(None, _(u"Are you sure you want to delete this user from the database? This user will not appear in autocomplete results anymore."), _(u"Confirm"), wx.YES_NO|wx.ICON_QUESTION).ShowModal()

def get_ignored_client():
    entry = wx.TextEntryDialog(None, _(u"Enter the name of the client : "), _(u"Add client"))
    if entry.ShowModal() == wx.ID_OK:
        return entry.GetValue()
    return None

def clear_list():
    dlg = wx.MessageDialog(None, _(u"Do you really want to empty this buffer? It's  items will be removed from the list but not from Twitter"), _(u"Empty buffer"), wx.ICON_QUESTION|wx.YES_NO)
    return dlg.ShowModal()

def remove_buffer():
    return wx.MessageDialog(None, _(u"Do you really want to destroy this buffer?"), _(u"Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def user_not_exist():
    return wx.MessageDialog(None, _(u"That user does not exist"), _(u"Error"), wx.ICON_ERROR).ShowModal()

def timeline_exist():
    return wx.MessageDialog(None, _(u"A timeline for this user already exists. You can't open another"), _(u"Existing timeline"), wx.ICON_ERROR).ShowModal()

def no_tweets():
    return wx.MessageDialog(None, _(u"This user has no tweets, so you can't open a timeline for them."), _(u"Error!"), wx.ICON_ERROR).ShowModal()

def protected_user():
    return wx.MessageDialog(None, _(u"This is a protected Twitter user, which means you can't open a timeline using the Streaming API. The user's tweets will not update due to a twitter policy. Do you want to continue?"), _(u"Warning"), wx.ICON_WARNING|wx.YES_NO).ShowModal()

def no_following():
    return wx.MessageDialog(None, _(u"This is a protected user account, you need to follow this user to view their tweets or likes."), _(u"Error"), wx.ICON_ERROR).ShowModal()

def donation():
    dlg = wx.MessageDialog(None, _(u"If you like {0} we need your help to keep it going. Help us by donating to the project. This will help us pay for the server, the domain and some other things to ensure that {0} will be actively maintained. Your donation will give us the means to continue the development of {0}, and to keep {0} free. Would you like to donate now?").format(application.name), _(u"We need your help"), wx.ICON_QUESTION|wx.YES_NO)
    return dlg.ShowModal()

def no_tweets():
    return wx.MessageDialog(None, _(u"This user has no tweets. {0} can't create a timeline.").format(application.name), _(u"Error"), wx.ICON_ERROR).ShowModal()

def no_favs():
    return wx.MessageDialog(None, _(u"This user has no favorited tweets. {0} can't create a timeline.").format(application.name), _(u"Error"), wx.ICON_ERROR).ShowModal()

def no_followers():
    return wx.MessageDialog(None, _(u"This user has no followers. {0} can't create a timeline.").format(application.name), _(u"Error"), wx.ICON_ERROR).ShowModal()

def no_friends():
    return wx.MessageDialog(None, _(u"This user has no friends. {0} can't create a timeline.").format(application.name), _(u"Error"), wx.ICON_ERROR).ShowModal()

def view_geodata(geotext):
    """Specific message dialog to display geolocation data"""
    return wx.MessageDialog(None, _(u"Geolocation data: {0}").format(geotext), _(u"Geo data for this tweet")).ShowModal()

def changed_keymap():
    return wx.MessageDialog(None, _(u"TWBlue has detected that you're running windows 10 and has changed the default keymap to the Windows 10 keymap. It means that some keyboard shorcuts could be different. Please check the keystroke editor by pressing Alt+Win+K to see all available keystrokes for this keymap."), _(u"Information"), wx.OK).ShowModal()

def unauthorized():
    return wx.MessageDialog(None, _(u"You have been blocked from viewing  this content"), _(u"Error"), wx.OK).ShowModal()

def blocked_timeline():
    return wx.MessageDialog(None, _(u"You have been blocked from viewing  someone's content. In order to avoid conflicts with the full session, TWBlue will remove the affected timeline."), _(u"Error"), wx.OK).ShowModal()

def suspended_user():
    return wx.MessageDialog(None, _(u"TWBlue cannot load this timeline because the user has been suspended from Twitter."), _(u"Error"), wx.OK).ShowModal()

def delete_filter():
    return wx.MessageDialog(None, _(u"Do you really want to delete this filter?"), _(u"Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def existing_filter():
    return wx.MessageDialog(None, _(u"This filter already exists. Please use a different title"), _(u"Error"), wx.OK).ShowModal()

def common_error(reason):
    return wx.MessageDialog(None, reason, _(u"Error"), wx.OK).ShowModal()

def invalid_configuration():
    return wx.MessageDialog(None, _("The configuration file is invalid."), _("Error"), wx.ICON_ERROR).ShowModal()

def dead_pid():
    return wx.MessageDialog(None, _(u"{0} quit unexpectedly the last time it was run. If the problem persists, please report it to the {0} developers.").format(application.name), _(u"Warning"), wx.OK).ShowModal()

