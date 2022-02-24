class UsersController < ApplicationController
    before_action :set_user, only: [:show, :edit, :update, :create]
    
    def new
        @user = User.new
    end

    def edit
        
    end

    def update
        if @user.update(user_params)
            flash[:notice] = "Your account has been successfully updated!"
            redirect_to profiles_path
        else
            render 'edit'
        end
    end
      
    def create
        if @user.save
            session[:user_id] = @user.id
            redirect_to profiles_path, notice: "You have successfully signed up!"
        else
            render "new"
        end
    end

    private
    def user_params
        params.permit(:email, :password, :password_confirmation)
    end

    def set_user
        @user = User.new(user_params)
    end
end
