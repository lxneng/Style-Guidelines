CSS Code Guideline
====================



- 尽可能的通过继承和层叠重用已有的样式

- 单条CSS规则的书写格式要求 

  - 属性要写在一行
  - 需要在 "{" 和 "}" 前后加空格
  - 多个selector各占一行

    .. code-block:: css 

     .selector1,
     .selector2,
     .selector3 { property:value; }

  - 兼容多个浏览器时，将标准属性写在后面

    .. code-block:: css

      -webkit-border-radius:4px;-moz-border-radius:4px;border-radius: 4px;


  - 注释的格式

    .. code-block:: css
    
      /* =home-page
      ---------------------------------------------- */
        /* =intro
          ---------------------------------------------- */
        #home-page #intro {
            ...
        }
        /* ------------------------------------------- */

        /* =featured articles & popular articles
          ---------------------------------------------- */
        #home-page #featured-articles, #home-page #popular-articles {
            ...
        }
        /* ------------------------------------------- */
      /* ------------------------------------------- */  
       

- ID和Class命名。命名不要用缩写，单词间用"-"做为连接符

  - ID是用来标识具体模块，命名必须具体且唯一，由前缀和名字组成。不要滥用ID。如： `#db-video-list` 。
  - Class是用来标识某一类型的元素，命名简洁表意清楚。如：`.list`。
  - 推荐使用的class名
  
    +--------------+----------------------------------------------------+
    | 表示状态     | `.on, .active, selected, .hili`                    |
    +--------------+----------------------------------------------------+
    | 表示位置     | `.first, .last, .main, .side`                      |
    +--------------+----------------------------------------------------+
    | 表示结构     | `.hd, .bd, .ft, .col, .section`                    |
    +--------------+----------------------------------------------------+
    | 通用元素     | `.tb, .frm, .nav, .list, .item, .tag, .pic, .info` |
    +--------------+----------------------------------------------------+

- 尽量避免使用CSS Hack

  - 推荐使用下面的

    +-----------+--------------------+
    | IE6       | `_property:value`  |
    +-----------+--------------------+
    | IE6/7     | `*property:value`  |
    +-----------+--------------------+
    | IE6/7/8/9 | `property:value\9` |
    +-----------+--------------------+
    | 非IE6     | `property//:value` |
    +-----------+--------------------+
  
  - 区别规则
  
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | IE6                  | `* html selector { ... }`                                                                                      |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | IE7                  | `*:first-child+html selector { ... }`                                                                          |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | 非IE6                | `html>body selector { ... }`                                                                                   |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | firefox only         | `@-moz-document url-prefix() { ... }`                                                                          |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | saf3+/chrome1+       | `@media all and (-webkit-min-device-pixel-ratio:0) { ... }`                                                    |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | opera only           | `@media all and (-webkit-min-device-pixel-ratio:10000),not all and (-webkit-min-device-pixel-ratio:0) { ... }` |
    +----------------------+----------------------------------------------------------------------------------------------------------------+
    | iPhone/mobile webkit | `@media screen and (max-device-width: 480px) { ... }`                                                          |
    +----------------------+----------------------------------------------------------------------------------------------------------------+



- 使用`after`或`overflow`的方式清浮动

- 内联和外联的CSS都必须放在页面的head里。顺序是：全站级CSS，产品级CSS，页面级(外联)CSS，页面级(内联)CSS，内联CSS

- 避免使用低效的选择器

    例如
  
    .. code-block:: css 
  
      body > * {...}
      ul > li > a {...}
      #footer > h3 {...}
      ul#top_blue_nav {...}
      #searbar span.submit a { ... }

- 尽量避免使用filter

- 不要直接修改标签的样式

  如:    `div { ... }`


- 不要在标签上直接写样式

  如: `<div style="margin-bottom:30px;">` 

- 不要在CSS中使用 `expression`

- 不要在CSS中使用 `@import` 

- 不要在CSS中使用 `!important`

- 绝对不要在CSS中使用 "*" 选择符 

Links
------

    - `豆瓣CSS开发规范 <http://goo.gl/K3W2g>`_
    - `inuit.css is a pragmatic, production-ready CSS framework. <https://github.com/csswizardry/inuit.css>`_
    - `How to Manage CSS Explosion <http://stackoverflow.com/questions/2253110/how-to-manage-css-explosion>`_
    - `Best Practices - CSS Stylesheet Formatting <http://stackoverflow.com/questions/956996/best-practices-css-stylesheet-formatting>`_
    - `CSS Standards & Best Practices <http://www.dezinerfolio.com/2009/02/20/css-standards-best-practices>`_
    - `Create Maintainable Code with a CSS Styleguide <http://www.louddog.com/2008/create-maintainable-code-with-a-css-styleguide/>`_
    - `CSS Best Practices <http://www.evotech.net/blog/2007/04/css-best-practices/>`_
