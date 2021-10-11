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
	  'hoob3rt/lualine.nvim',
	  requires = {'kyazdani42/nvim-web-devicons', opt = true}
	}
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
	use 'neoclide/coc.nvim'
	use 'rust-lang/rust.vim';
end)
