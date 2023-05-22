/*
* Vimeo Embed Plugin
*
* @author David Thenon <dthenon@emencia.com>
* @version 1.1.0
*
* Original code comes from CKeditor Youtube plugin version 2.1.10:
* https://github.com/fonini/ckeditor-youtube-plugin
*/
(function () {
    CKEDITOR.plugins.add('vimeo', {
        lang: [ 'en', 'fr' ],
        init: function (editor) {
            editor.addCommand('vimeo', new CKEDITOR.dialogCommand('vimeo', {
                allowedContent: 'div{*}(*); iframe{*}[!width,!height,!src,!frameborder,!allowfullscreen]; object param[*]; a[*]; img[*]'
            }));

            editor.ui.addButton('Vimeo', {
                label : editor.lang.vimeo.button,
                toolbar : 'insert',
                command : 'vimeo',
                icon : this.path + 'images/icon.svg'
            });

            CKEDITOR.dialog.add('vimeo', function (instance) {
                var video,
                    disabled = editor.config.vimeo_disabled_fields || [];

                return {
                    title : editor.lang.vimeo.title,
                    minWidth : 510,
                    minHeight : 200,
                    onShow: function () {
                        for (var i = 0; i < disabled.length; i++) {
                            this.getContentElement('vimeoPlugin', disabled[i]).disable();
                        }
                    },
                    contents :
                        [{
                            id : 'vimeoPlugin',
                            expand : true,
                            elements :
                                [{
                                    id : 'txtEmbed',
                                    type : 'textarea',
                                    label : editor.lang.vimeo.txtEmbed,
                                    onChange : function (api) {
                                        vimeoHandleEmbedChange(this, api);
                                    },
                                    onKeyUp : function (api) {
                                        vimeoHandleEmbedChange(this, api);
                                    },
                                    validate : function () {
                                        if (this.isEnabled()) {
                                            if (!this.getValue()) {
                                                alert(editor.lang.vimeo.noCode);
                                                return false;
                                            }
                                            else
                                            if (this.getValue().length === 0 || this.getValue().indexOf('//') === -1) {
                                                alert(editor.lang.vimeo.invalidEmbed);
                                                return false;
                                            }
                                        }
                                    }
                                },
                                {
                                    type : 'html',
                                    html : editor.lang.vimeo.or + '<hr>'
                                },
                                {
                                    type : 'hbox',
                                    widths : [ '70%', '15%', '15%' ],
                                    children :
                                    [
                                        {
                                            id : 'txtUrl',
                                            type : 'text',
                                            label : editor.lang.vimeo.txtUrl,
                                            onChange : function (api) {
                                                vimeoHandleLinkChange(this, api);
                                            },
                                            onKeyUp : function (api) {
                                                vimeoHandleLinkChange(this, api);
                                            },
                                            validate : function () {
                                                if (this.isEnabled()) {
                                                    if (!this.getValue()) {
                                                        alert(editor.lang.vimeo.noCode);
                                                        return false;
                                                    }
                                                    else{
                                                        video = vimeoVidId(this.getValue());

                                                        if (this.getValue().length === 0 ||  video === false)
                                                        {
                                                            alert(editor.lang.vimeo.invalidUrl);
                                                            return false;
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        {
                                            type : 'text',
                                            id : 'txtWidth',
                                            width : '60px',
                                            label : editor.lang.vimeo.txtWidth,
                                            'default' : editor.config.vimeo_width != null ? editor.config.vimeo_width : '640',
                                            validate : function () {
                                                if (this.getValue()) {
                                                    var width = parseInt (this.getValue()) || 0;

                                                    if (width === 0) {
                                                        alert(editor.lang.vimeo.invalidWidth);
                                                        return false;
                                                    }
                                                }
                                                else {
                                                    alert(editor.lang.vimeo.noWidth);
                                                    return false;
                                                }
                                            }
                                        },
                                        {
                                            type : 'text',
                                            id : 'txtHeight',
                                            width : '60px',
                                            label : editor.lang.vimeo.txtHeight,
                                            'default' : editor.config.vimeo_height != null ? editor.config.vimeo_height : '360',
                                            validate : function () {
                                                if (this.getValue()) {
                                                    var height = parseInt(this.getValue()) || 0;

                                                    if (height === 0) {
                                                        alert(editor.lang.vimeo.invalidHeight);
                                                        return false;
                                                    }
                                                }
                                                else {
                                                    alert(editor.lang.vimeo.noHeight);
                                                    return false;
                                                }
                                            }
                                        }
                                    ]
                                },
                                {
                                    type : 'hbox',
                                    widths : [ '55%', '45%' ],
                                    children :
                                    [
                                        {
                                            id : 'chkResponsive',
                                            type : 'checkbox',
                                            label : editor.lang.vimeo.txtResponsive,
                                            'default' : editor.config.vimeo_responsive != null ? editor.config.vimeo_responsive : false
                                        },
                                        {
                                            id : 'chkAutoplay',
                                            type : 'checkbox',
                                            'default' : editor.config.vimeo_autoplay != null ? editor.config.vimeo_autoplay : false,
                                            label : editor.lang.vimeo.chkAutoplay
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    onOk: function()
                    {
                        var content = '';
                        var responsiveStyle = '';

                        if (this.getContentElement('vimeoPlugin', 'txtEmbed').isEnabled()) {
                            content = this.getValueOf('vimeoPlugin', 'txtEmbed');
                        }
                        else {
                            var url = 'https://', params = [], startSecs;
                            var width = this.getValueOf('vimeoPlugin', 'txtWidth');
                            var height = this.getValueOf('vimeoPlugin', 'txtHeight');

                            url += 'player.vimeo.com/video/' + video;

                            // Never display portrait/title/signature
                            params.push('portrait=0');
                            params.push('title=0');
                            params.push('byline=0');

                            if (this.getContentElement('vimeoPlugin', 'chkAutoplay').getValue() === true) {
                                params.push('autoplay=1');
                            }

                            if (params.length > 0) {
                                url = url + '?' + params.join('&');
                            }

                            if (this.getContentElement('vimeoPlugin', 'chkResponsive').getValue() === true) {
                                content += '<div class="ratio ratio-16x9">';
                            }

                            content += '<iframe width="' + width + '" height="' + height + '" src="' + url + '" ' + responsiveStyle;
                            content += 'allowfullscreen></iframe>';

                            if (this.getContentElement('vimeoPlugin', 'chkResponsive').getValue() === true) {
                                content += '</div>';
                            }
                        }

                        var element = CKEDITOR.dom.element.createFromHtml(content);
                        var instance = this.getParentEditor();
                        instance.insertElement(element);
                    }
                };
            });
        }
    });
})();

function vimeoHandleLinkChange(el, api) {
    var video = vimeoVidId(el.getValue());

    if (el.getValue().length > 0) {
        el.getDialog().getContentElement('vimeoPlugin', 'txtEmbed').disable();
    }
    else {
        el.getDialog().getContentElement('vimeoPlugin', 'txtEmbed').enable();
    }
}

function vimeoHandleEmbedChange(el, api) {
    if (el.getValue().length > 0) {
        el.getDialog().getContentElement('vimeoPlugin', 'txtUrl').disable();
    }
    else {
        el.getDialog().getContentElement('vimeoPlugin', 'txtUrl').enable();
    }
}


/**
* JavaScript function to match (and return) the video Id
* of any valid Vimeo Url, given as input string.
*/
function vimeoVidId(url) {
    var p = /^(?:https?:\/\/)?(?:player\.vimeo\.com\/video\/|vimeo\.com\/)(\d+)(?:\S+)?$/;
    return (url.match(p)) ? RegExp.$1 : false;
}
