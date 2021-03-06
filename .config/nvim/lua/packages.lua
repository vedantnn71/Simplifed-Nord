require('packer').startup(function()
	use 'wbthomason/packer.nvim'
	use 'arcticicestudio/nord-vim'
	use {
	'vimwiki/vimwiki',
	config = function() 
	    vim.g.vimwiki_ext2syntax = {
		['.md'] = 'markdown',
		['.markdown'] = 'markdown',
		['.mdown'] = 'markdown',
	    }
	end
	}
	use {
	  'nvim-lualine/lualine.nvim',
	  requires = {'kyazdani42/nvim-web-devicons', opt = true}
	}
        use 'stevearc/dressing.nvim'
        use 'luochen1990/rainbow'
	use {
		'bluz71/vim-moonfly-statusline',
		config = function()
                    vim.g.moonflyCursorColor = 1
                    vim.g.moonflyItalics = 0
                end
        }
	use 'vim-syntastic/syntastic'
	use {
	  'nvim-telescope/telescope.nvim',
	  requires = {
		  {'nvim-lua/plenary.nvim'}
	  }
	}
	use 'prettier/vim-prettier'
	use 'rust-lang/rust.vim';
        use 'pangloss/vim-javascript'
        use 'leafgarland/typescript-vim'
        use 'mattn/emmet-vim'
        use 'peitalin/vim-jsx-typescript'
        use {
            'styled-components/vim-styled-components'
        }
        use {'neoclide/coc.nvim', branch = 'release'}
        use {'mg979/vim-visual-multi'}
        use 'tpope/vim-surround'
        use 'akinsho/toggleterm.nvim'
        use 'skanehira/denops-docker.vim'
        use 'tmhedberg/SimpylFold'
        use 'MaxMEllon/vim-jsx-pretty'
        use 'jparise/vim-graphql'
        use 'hail2u/vim-css3-syntax'
        use 'ap/vim-css-color'
        use 'karb94/neoscroll.nvim'
        use 'ryanoasis/vim-devicons'
        use 'dart-lang/dart-vim-plugin'
end)
