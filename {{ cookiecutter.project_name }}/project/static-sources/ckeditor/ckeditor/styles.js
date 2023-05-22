/**
* Copyright (c) 2003-2017, CKSource - Frederico Knabben. All rights reserved.
* For licensing, see LICENSE.md or http://ckeditor.com/license
*
* This is a customized version by Emencia, cloned from django-ckeditor and edited
*/

// This file contains style definitions that can be used by CKEditor plugins.
//
// The most common use for it is the "stylescombo" plugin which shows the Styles drop-down
// list containing all styles in the editor toolbar. Other plugins, like
// the "div" plugin, use a subset of the styles for their features.
//
// If you do not have plugins that depend on this file in your editor build, you can simply
// ignore it. Otherwise it is strongly recommended to customize this file to match your
// website requirements and design properly.
//
// For more information refer to: http://docs.ckeditor.com/#!/guide/dev_styles-section-style-rules

CKEDITOR.stylesSet.add( 'default', [
    /* Block styles */
//     { name: 'Italic Title',		element: 'h2', styles: { 'font-style': 'italic' } },
//     { name: 'Subtitle',			element: 'h3', styles: { 'color': '#aaa', 'font-style': 'italic' } },
//     {
//         name: 'Special Container',
//         element: 'div',
//         styles: {
//             padding: '5px 10px',
//             background: '#eee',
//             border: '1px solid #ccc'
//         }
//     },

    /* Inline styles */
//     { name: 'Marker',			element: 'span', attributes: { 'class': 'marker' } },

//     { name: 'Small',			element: 'small' },
    { name: 'Typewriter',		element: 'tt' },

    { name: 'Computer Code',	element: 'code' },

    { name: 'Deleted Text',		element: 'del' },
    { name: 'Inserted Text',	element: 'ins' },

    { name: 'Cited Work',		element: 'cite' },

    { name: 'Flex video',		element: 'div', attributes: { 'class': 'flex-video widescreen' } },

    /* Object styles */

    {
        name: 'Styled Image (left)',
        element: 'img',
        attributes: { 'class': 'left' }
    },

    {
        name: 'Styled Image (right)',
        element: 'img',
        attributes: { 'class': 'right' }
    },

//     {
//         name: 'Compact Table',
//         element: 'table',
//         attributes: {
//             cellpadding: '5',
//             cellspacing: '0',
//             border: '1',
//             bordercolor: '#ccc'
//         },
//         styles: {
//             'border-collapse': 'collapse'
//         }
//     },

//     { name: 'Borderless Table',		element: 'table',	styles: { 'border-style': 'hidden', 'background-color': '#E6E6FA' } },
//     { name: 'Square Bulleted List',	element: 'ul',		styles: { 'list-style-type': 'square' } },

    /* Widget styles */

//     { name: 'Clean Image', type: 'widget', widget: 'image', attributes: { 'class': 'image-clean' } },
//     { name: 'Grayscale Image', type: 'widget', widget: 'image', attributes: { 'class': 'image-grayscale' } },
//
//     { name: 'Featured Snippet', type: 'widget', widget: 'codeSnippet', attributes: { 'class': 'code-featured' } },
//
//     { name: 'Featured Formula', type: 'widget', widget: 'mathjax', attributes: { 'class': 'math-featured' } },
//
//     { name: '240p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-240p' }, group: 'size' },
//     { name: '360p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-360p' }, group: 'size' },
//     { name: '480p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-480p' }, group: 'size' },
//     { name: '720p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-720p' }, group: 'size' },
//     { name: '1080p', type: 'widget', widget: 'embedSemantic', attributes: { 'class': 'embed-1080p' }, group: 'size' },
//
//     // Adding space after the style name is an intended workaround. For now, there
//     // is no option to create two styles with the same name for different widget types. See http://dev.ckeditor.com/ticket/16664.
//     { name: '240p ', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-240p' }, group: 'size' },
//     { name: '360p ', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-360p' }, group: 'size' },
//     { name: '480p ', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-480p' }, group: 'size' },
//     { name: '720p ', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-720p' }, group: 'size' },
//     { name: '1080p ', type: 'widget', widget: 'embed', attributes: { 'class': 'embed-1080p' }, group: 'size' }

] );

