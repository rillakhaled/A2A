Rails.application.routes.draw do
  root "pages#about"
  resources :images
  resources :users
  resources :sessions
  resources :profiles
  get 'signup', to: 'users#new', as: 'signup'
  get 'login', to: 'sessions#new', as: 'login'
  get 'logout', to: 'sessions#destroy', as: 'logout'
  get 'about', to: 'pages#index'
end
