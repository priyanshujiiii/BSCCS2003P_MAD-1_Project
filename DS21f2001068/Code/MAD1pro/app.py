###################################################################################


##########                        Code  Structure                  ################

##########                        1) Library Import                ################
##########                        2) Flask Configurations          ################
##########                        3) Database                      ################
##########                        5) Home Page                     ################
##########                        5) Sponser                       ################
##########                        6) Influencer                    ################
##########                        7) Admin                         ################


###################################################################################


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                         1) Library Import               ################


###################################################################################


import os
from flask import Flask, render_template, request, redirect, url_for, flash,jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from sqlalchemy import func
from werkzeug.utils import secure_filename
from time import sleep
from flask import redirect, abort
from sqlalchemy.orm import relationship
from flask import flash
from sqlalchemy import desc


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                    2)Flask Configurations               ################


###################################################################################


app = Flask(__name__)

current_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "oeanalytics.sqlite3") 
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
global userrun


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                         3) Database                     ################


###################################################################################



class Admin(db.Model):
    user_id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

class Campaign(db.Model):
    campaignid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    campaignname = db.Column(db.String, nullable=False)
    category = db.Column(db.String, db.ForeignKey('category.category'), nullable=False)
    goals = db.Column(db.String, nullable=False)
    userid = db.Column(db.String, db.ForeignKey('sponsor.username'), nullable=False)
    campaign_description = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    visibility = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    alloted = db.Column(db.Integer, nullable=False)
    payment = db.Column(db.Integer, nullable=False)

class Category(db.Model):
    category = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

class Influencer(db.Model):
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    contact = db.Column(db.Numeric, nullable=False)
    district = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    pincode = db.Column(db.Numeric, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    instagram_id = db.Column(db.String, nullable=False)
    linkedin_id = db.Column(db.String, nullable=False)
    facebook_id = db.Column(db.String, nullable=False)
    x_id = db.Column(db.String, nullable=False)
    category = db.Column(db.String, db.ForeignKey('category.category'), nullable=False)
    insta_f = db.Column(db.Integer, nullable=False)
    linkedin_f = db.Column(db.Integer, nullable=False)
    facebook_f = db.Column(db.Integer, nullable=False)
    x_f = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String, nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    wallet = db.Column(db.Integer, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    influencer_u = db.Column(db.String, db.ForeignKey('influencer.username'), nullable=False)
    sponser_u = db.Column(db.String, db.ForeignKey('sponsor.username'), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.campaignid'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    campaign_name = db.Column(db.String, nullable=False)

class Request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    influencer_u = db.Column(db.String, db.ForeignKey('influencer.username'), nullable=False)
    sponser_u = db.Column(db.String, db.ForeignKey('sponsor.username'), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.campaignid'), nullable=False)
    campaign_name = db.Column(db.String, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    payment_amount = db.Column(db.Integer, nullable=False)
    requirements = db.Column(db.String, nullable=False)
    messages = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    category = db.Column(db.String, db.ForeignKey('category.category'), nullable=False)

class Sponsor(db.Model):
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    district = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    industry = db.Column(db.String, nullable=False)
    positions = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    wallet = db.Column(db.Integer, nullable=False)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                        4) Home Page                        #############


###################################################################################

# 4.0.1 App initilization
@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('oeanalytics'))

# 4.0.2 Redirecting App
@app.route('/oeanalytics', methods=['GET', 'POST'])
def oeanalytics():
    return render_template('index.html')

# 4.1 Influencer signup form redirection
@app.route('/oeanalytics/influencer_signup', methods=['GET', 'POST'])
def influencer_signup():
    categories = Category.query.all()
    return render_template('influencer_signup.html',categories=categories)

# 4.1.1 Influencer signup commit actions
@app.route('/oeanalytics/influencer_signupp', methods=['GET', 'POST'])
def influencer_signupp():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        address = request.form.get('address')
        district = request.form.get('district')
        bio = request.form.get('bio')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        contact = request.form.get('contact')
        instagram_id = request.form.get('instagram_id')
        linkedin_id = request.form.get('linkedin_id')
        facebook_id = request.form.get('facebook_id')
        x_id = request.form.get('x_id')
        category = request.form.get('category')
        insta_f = request.form.get('insta_f')
        linkedin_f = request.form.get('linkedin_f')
        facebook_f = request.form.get('facebook_f')
        x_f = request.form.get('x_f')
        # Validate and process the form data here (e.g., save to database)
        user_i = Influencer.query.filter_by(username=username).first()
        if user_i:
            flash('User Name Exist', 'danger')
            return redirect(url_for('oeanalytics'))
        else:
            new_influencer = Influencer(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                address=address,
                district=district,
                state=state,
                pincode=pincode,
                contact=contact,
                instagram_id=instagram_id,
                linkedin_id=linkedin_id,
                facebook_id=facebook_id,
                bio=bio,
                x_id=x_id,
                category=category,
                insta_f=insta_f,
                linkedin_f=linkedin_f,
                facebook_f=facebook_f,
                x_f=x_f,
                flag=0,
                wallet=0
            )
            # Save image to static/images folder

            # Add to database
            db.session.add(new_influencer)
            db.session.commit()
            
            flash('Signup successful!', 'success')
            return redirect(url_for('signin'))

# 4.2 Sponsor signup form redirection
@app.route('/oeanalytics/sponsor_signup', methods=['GET', 'POST'])
def sponsor_signup():
    categories = Category.query.all()
    return render_template('sponsor_signup.html',categories=categories)

# 4.2.1 Sponsor signup
@app.route('/oeanalytics/sponser_signupp', methods=['GET', 'POST'])
def sponser_signupp():
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    address = request.form.get('address')
    district = request.form.get('district')
    bio = request.form.get('bio')
    state = request.form.get('state')
    pincode = request.form.get('pincode')
    contact = request.form.get('contact')
    company_name = request.form.get('company_name')
    industry = request.form.get('industry')
    positions = request.form.get('positions')
    # Handle file uploads
    user_i = Sponsor.query.filter_by(username=username).first()
    if user_i:
        flash('User Name Exist', 'danger')
        return redirect(url_for('oeanalytics'))
    else:
        new_sponser = Sponsor(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            district=district,
            state=state,
            pincode=pincode,
            contact=contact,
            company_name=company_name,
            industry=industry,
            positions=positions,
            bio=bio,
            flag = 0,
            wallet=0
        )

        db.session.add(new_sponser)
        db.session.commit()
                
        flash('Signup successful!', 'success')
        return redirect(url_for('signin'))

# 4.3 Signin page redirection
@app.route('/oeanalytics/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

# 4.3.1 login and page redirection
@app.route('/oeanalytics/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    userrole = request.form.get('user_role')
    userrun = username
    session['username'] =username
    if userrole == "admin" :
        user_a = Admin.query.filter_by(user_id=username, password=password).first()
        if user_a:
            flash('Access Granted','success')
            return redirect(url_for('admin_home'))
        else:
            flash('Wrong Credential','danger')
            redirect(url_for('oeanalytics'))
        
    if userrole == "influencer" :
        user_i = Influencer.query.filter_by(username=username, password=password).first()
        if user_i:
            if user_i.flag==1:
                flash('your id is flagged by admin','danger')
                return redirect(url_for('oeanalytics'))
            else:
                return redirect(url_for('influencer_home'))
        else:
            flash('Wrong Credential','danger')
            return redirect(url_for('oeanalytics'))
    if userrole == "sponsor" :
        user_s = Sponsor.query.filter_by(username=username, password=password).first()
        if user_s:
            if user_s.flag==1:
                flash('your id is flagged by admin','danger')
                return redirect(url_for('oeanalytics'))
            else:
                flash('Access Granted','success')
                return redirect(url_for('sponsor_home'))
        else:
            flash('Wrong Credential','danger')
            return redirect(url_for('oeanalytics'))
        
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

###################################################################################


##########                      5) Sponser                   ######################


###################################################################################


# 5.1  My Campaign
@app.route('/oeanalytics/sponsor/')
def sponsor_home():
    return render_template('sponsor_home.html')


# 5.1.A
@app.route('/oeanalytics/sponsor/dashboard/plan/<int:value>')
def choose_plan(value):
    categories = Category.query.all()
    return render_template('sponsor_dashboard.html', template='plan.html',categories=categories,value=value)

# 5.1.B
@app.route('/oeanalytics/sponsor/dashboard/plan/<int:value>/add_campaign/', methods=['GET', 'POST'])
def add_plan(value):
    if request.method == 'POST':
        # Extract form data
        campaign_name = request.form.get('campaignName')
        category = request.form.get('category')
        goals = request.form.get('goals')
        userid = request.form.get('userid')
        campaign_description = request.form.get('campaignDescription')
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')
        visibility = request.form.get('visibility')
        budget = value

        
        new_campaign = Campaign(
            campaignname=campaign_name,
            category=category,
            goals=goals,
            userid=session['username'],
            campaign_description=campaign_description,
            start_date=start_date,
            end_date=end_date,
            visibility=visibility,
            budget=budget,
            alloted=0,
            flag=0,
            payment=0
        )

        db.session.add(new_campaign)
        db.session.commit()
        flash(f'Campaign "{campaign_name}" added successfully!', 'success')
        return redirect(url_for('my_campaign'))
# 5.1.0
@app.route('/oeanalytics/sponsor/dashboard/<template>')
def sponsor_dashboard(template):
    categories = Category.query.all()
    influencer = Influencer.query.all()
    return render_template('sponsor_dashboard.html', template=template,categories=categories,influencers=influencer)

# 5.1.1
@app.route('/oeanalytics/sponsor/dashboard/campaign/', methods=['POST','GET'])
def my_campaign():
    if session['username']:
        print(session['username'])
        campaigns = db.session.query(Campaign).filter(Campaign.userid == session['username']).all()
        return render_template('sponsor_dashboard.html', template='my_Campaign.html',campaigns=campaigns)
    else:
        return render_template('signin.html')

# 5.1.1.1.A
@app.route('/oeanalytics/sponsor/dashboard/campaign/edit/<int:campaign_id>', methods=['POST','GET'])
def edit_campaign(campaign_id):
    categories = Category.query.all()
    campaign = db.session.query(Campaign).filter(Campaign.campaignid == campaign_id).first()
    return render_template('sponsor_dashboard.html', template='editcampaign.html',categories=categories,campaign=campaign)

# 5.1.1.1.B
@app.route('/oeanalytics/sponsor/dashboard/campaign/edit/update/<int:campaign_id>', methods=['POST', 'GET'])
def update_campaign(campaign_id):
    # Fetch the campaign object to be updated
    campaign = Campaign.query.get_or_404(campaign_id)

    # Update the campaign fields
    campaign.campaignname = request.form.get('campaignName') or campaign.campaignname
    campaign.category = request.form.get('category') or campaign.category
    campaign.goals = request.form.get('goals') or campaign.goals
    campaign.userid = request.form.get('userid') or campaign.userid
    campaign.campaign_description = request.form.get('campaignDescription') or campaign.campaign_description
    campaign.start_date = request.form.get('startDate') or campaign.start_date
    campaign.end_date = request.form.get('endDate') or campaign.end_date
    campaign.visibility = request.form.get('visibility') or campaign.visibility
    campaign.budget = request.form.get('budget') or campaign.budget

    # Commit changes to the database
    db.session.commit()
    flash('Campaign updated successfully', 'success')

    # Redirect to the dashboard or any other desired route
    return redirect(url_for('my_campaign'))

# 5.1.1.2
@app.route('/oeanalytics/sponsor/dashboard/campaign/delete/<int:campaign_id>', methods=['POST','GET'])
def delete_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)

    # Delete related records in the Request table
    Request.query.filter(Request.campaign_id == campaign_id).delete()

    # Now delete the campaign
    db.session.delete(campaign)
    db.session.commit()
    flash('deleted','danger')
    return redirect(url_for('my_campaign'))

# 5.1.1.3
@app.route('/oeanalytics/sponsor/dashboard/campaign/view_campaign/<int:campaign_id>',methods=['POST','GET'])
def view_campaign(campaign_id):
    if 'username' in session:
        campaign = db.session.query(Campaign).filter(Campaign.campaignid == campaign_id).first()
        requests_outgoing = Request.query.filter_by(sponser_u=session['username'],role='Sponser',campaign_id=campaign_id).all()
        requests_incoming = Request.query.filter_by(sponser_u=session['username'],role='Influencer',campaign_id=campaign_id).all()
        requests = Request.query.filter_by(campaign_id=campaign_id).all()
        accepted_request = next((req for req in requests if req.status == 1), None)
        payment = Payment.query.filter_by(campaign_id=campaign_id).first()
        status = 0
        if campaign.flag == 1:
            influencer = Influencer.query.all()
            return render_template('sponsor_dashboard.html', template='viewCampaign.html',campaign=campaign,status=4,requests_outgoing=requests_outgoing,requests_incoming=requests_incoming,influencer=influencer,payment=payment)
        else:    
            if accepted_request:
            # Fetch influencer details
                influencer = Influencer.query.get(accepted_request.influencer_u)
                return render_template('sponsor_dashboard.html', template='viewCampaign.html',campaign=campaign,status=1,requests_outgoing=requests_outgoing,requests_incoming=requests_incoming,influencer=influencer,payment=payment)
            else:
                influencer = Influencer.query.all()
                return render_template('sponsor_dashboard.html', template='viewCampaign.html',campaign=campaign,status=5,requests_outgoing=requests_outgoing,requests_incoming=requests_incoming,influencer=influencer,payment=payment)
        
            
    else:
        return redirect(url_for('oeanalytics'))

# 5.2.B  New Campaign
@app.route('/oeanalytics/sponsor/dashboard/add_campaign/')
def addcampaign():
    categories = Category.query.all()
    return render_template('sponsor_dashboard.html', template='addcampaign.html',categories=categories)


# 5.2.B  New Campaign
@app.route('/add_campaign', methods=['GET', 'POST'])
def add_campaign():
    if request.method == 'POST':
        # Extract form data
        campaign_name = request.form.get('campaignName')
        category = request.form.get('category')
        goals = request.form.get('goals')
        userid = request.form.get('userid')
        campaign_description = request.form.get('campaignDescription')
        start_date = request.form.get('startDate')
        end_date = request.form.get('endDate')
        visibility = request.form.get('visibility')
        budget = request.form.get('budget')

        
        new_campaign = Campaign(
            campaignname=campaign_name,
            category=category,
            goals=goals,
            userid=session['username'],
            campaign_description=campaign_description,
            start_date=start_date,
            end_date=end_date,
            visibility=visibility,
            budget=budget,
            alloted=0,
            flag=0,
            payment=0
        )

        db.session.add(new_campaign)
        db.session.commit()
        flash('campaign created success fully','success')
        return render_template('sponsor_dashboard.html', template='template.html')

# 5.3  Incoming Ad Request
@app.route('/oeanalytics/sponsor/dashboard/incoming/<filter>', methods=['POST', 'GET'])
def incoming_sponser(filter):
    if filter == 'All':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Influencer').all()
        return render_template('sponsor_dashboard.html',template='incoming_sponser.html',requests = requests)
    if filter == 'Not Responded':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Influencer',status=0).all()
        return render_template('sponsor_dashboard.html',template='incoming_sponser.html',requests = requests)
    if filter == 'Accepted':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Influencer',status=1).all()
        return render_template('sponsor_dashboard.html',template='incoming_sponser.html',requests = requests)
    if filter == 'Rejected':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Influencer',status=2).all()
        return render_template('sponsor_dashboard.html',template='incoming_sponser.html',requests = requests)

# 5.3.1
@app.route('/oeanalytics/sponsor/dashboard/incoming/update/<int:request_id>/<int:new_status>', methods=['POST', 'GET'])
def update_request_sponser(request_id, new_status):
    request = Request.query.get(request_id)
    if not request:
        flash('Request not found', 'danger')
        return redirect(url_for('incoming_sponser', filter='All'))

    request.status = new_status
    db.session.commit()

    if new_status == 1:
        campaign = Campaign.query.get(request.campaign_id)
        if not campaign:
            flash('Campaign not found', 'danger')
            return redirect(url_for('incoming_sponser', filter='All'))

        campaign.alloted = 1
        db.session.commit()
        # Get the campaign_id from the updated request
        campaign_id = request.campaign_id

        # Step 3: Find other requests with the same campaign_id and status 0
        other_requests = Request.query.filter(
            Request.campaign_id == campaign_id,
            Request.status == 0
        ).all()

        # Step 4: Update these requests to status 3 (Ad Closed)
        for req in other_requests:
            req.status = 3
        db.session.commit()

        # Step 5: Create a new Payment record
        payment = Payment(
            influencer_u=request.influencer_u,
            sponser_u=session['username'],  # Assuming the sponsor's username is stored in the session
            campaign_id=campaign_id,
            amount=request.payment_amount,  # Assuming amount is part of the Request model or you need to define it
            status=0,  # Assuming initial status for the payment (e.g., 0 for pending)
            campaign_name=campaign.campaignname  # Assuming the campaign name is part of the Campaign model
        )
        db.session.add(payment)
        db.session.commit()
    flash('Accepted','success')
    requests = Request.query.filter_by(influencer_u=session['username'], role='Influencer').all()
    return redirect(url_for('incoming_sponser', filter='All'))


# 5.4  Outgoing Ad Request
@app.route('/oeanalytics/sponsor/dashboard/outgoing/<filter>', methods=['POST', 'GET'])
def outgoing_sponser(filter):
    if filter == 'All':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser').all()
        return render_template('sponsor_dashboard.html',template='outgoing_sponser.html',requests = requests)
    if filter == 'Not Responded':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser',status=0).all()
        return render_template('sponsor_dashboard.html',template='outgoing_sponser.html',requests = requests)
    if filter == 'Accepted':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser',status=1).all()
        return render_template('sponsor_dashboard.html',template='outgoing_sponser.html',requests = requests)
    if filter == 'Rejected':
        requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser',status=2).all()
        return render_template('sponsor_dashboard.html',template='outgoing_sponser.html',requests = requests)

# 5.4.1
@app.route('/oeanalytics/sponsor/dashboard/outgoing/delete/<int:request_id>', methods=['POST', 'GET'])
def delete_request_sponser(request_id):
    # Query the request by ID
    request_to_delete = Request.query.get(request_id)
    db.session.delete(request_to_delete)
    db.session.commit()
    flash('Request deleted successfully!', 'success')
    requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser',status=0).all()
    return redirect(url_for('outgoing_sponser',filter='All'))

# 5.4.2
@app.route('/oeanalytics/sponsor/dashboard/outgoing/edit/progress/<int:request_id>', methods=['POST', 'GET'])
def edit_request_sponser(request_id):
    requests = Request.query.get(request_id)
    requests.requirements = request.form.get('Requirements') or requests.requirements
    requests.messages = request.form.get('Message') or requests.messages
    requests.payment_amount = request.form.get('Amount') or requests.payment_amount
    db.session.commit()
    flash('edit request done successfully', 'success')
    requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser').all()
    return render_template('sponsor_dashboard.html',template='outgoing_sponser.html',requests = requests)

# 5.4.3
@app.route('/oeanalytics/sponsor/dashboard/outgoing/edit/<int:request_id>', methods=['POST', 'GET'])
def edit_page_sponser(request_id):
    requests = Request.query.get(request_id)
    return render_template('sponsor_dashboard.html',template ='edit_request_sponser.html',requests =requests )


# 5.5  Send Request
@app.route('/oeanalytics/sponsor/dashboard/sendrequest/',methods=['POST','GET'])
def sendrequest():
    if session['username']:
        print(session['username'])
        campaigns = db.session.query(Campaign).filter(Campaign.userid == session['username']).all()
        return render_template('sponsor_dashboard.html', template='senrequest.html',campaigns=campaigns)
    else:
        return render_template('signin.html')

# 5.5.1
@app.route('/oeanalytics/sponsor/dashboard/sendrequest/<int:campaign_id>', methods=['POST', 'GET'])
def s_request(campaign_id):
    # Get search parameters
    username = request.args.get('username', '')
    category = request.args.get('category', '')
    followers = request.args.get('followers', '')

    # Get all requests related to the campaign
    requests = Request.query.filter_by(campaign_id=campaign_id).all()

    # Get the list of influencer usernames from the filtered requests
    influencer_usernames = {req.influencer_u for req in requests}

    # Build the query for influencers
    query = Influencer.query.filter(
        ~Influencer.username.in_(influencer_usernames)
    )

    if username:
        query = query.filter(Influencer.username.like(f'%{username}%'))
    if category:
        query = query.filter(Influencer.category.like(f'%{category}%'))
    if followers:
        query = query.filter(
            (Influencer.insta_f >= int(followers)) |
            (Influencer.facebook_f >= int(followers)) |
            (Influencer.linkedin_f >= int(followers)) |
            (Influencer.x_f >= int(followers))
        )

    # Order by username
    influencers = query.order_by(Influencer.username).all()

    return render_template('sponsor_dashboard.html', template='request_campaign.html', influencers=influencers, campaign_id=campaign_id)


# 5.5.1.1
@app.route('/oeanalytics/sponsor/dashboard/sendrequest/influencer/<int:campaign_id>/<username>', methods=['POST', 'GET'])
def send_to_influencer(campaign_id, username):
    # Retrieve the Campaign and Influencer
    campaign = Campaign.query.get_or_404(campaign_id)
    influencer = Influencer.query.filter_by(username=username).first_or_404()
    
    
    # Create a new Request record
    new_request = Request(
        influencer_u=influencer.username,
        sponser_u= campaign.userid,  # You might want to get this from the session or user context
        campaign_id=campaign_id,
        campaign_name=campaign.campaignname,
        status=0,  # Set the initial status (e.g., 0 for pending)
        payment_amount=campaign.budget,  # Set the initial payment amount (could be updated later)
        requirements=campaign.goals,  # Provide additional requirements
        messages=campaign.campaign_description,  # Provide initial messages
        role='Sponser' , # Set the role, could be "sponsor" or something else
        category = campaign.category
    )

    # Add and commit the new request to the database
    db.session.add(new_request)
    db.session.commit()
    requests = Request.query.filter_by(campaign_id=campaign_id).all()

    # Get the list of influencer usernames from the filtered requests
    influencer_usernames = {req.influencer_u for req in requests}

    # Retrieve influencers whose usernames are not in the filtered requests
    influencers = Influencer.query.filter(
        ~Influencer.username.in_(influencer_usernames)
    ).all()
    flash(f"Request sent to {influencer.first_name} {influencer.last_name} for campaign '{campaign.campaignname}'.",'success')
    return render_template('sponsor_dashboard.html', template='request_campaign.html',influencers=influencers,campaign_id=campaign_id)

# 5.6 Payments
@app.route('/oeanalytics/sponsor/dashboard/payments')
def show_payments_sponser():
    sponsor_username = session.get('username')
    print(sponsor_username)  # Get the sponsor's username from the session
    # Filter payments by the sponsor's username
    payments = Payment.query.filter_by(sponser_u=sponsor_username).all()
    print(payments)
    return render_template('sponsor_dashboard.html', template='payment_sponser.html', payments=payments)

# 5.6.1
@app.route('/oeanalytics/sponsor/dashboard/payments/<int:payment_id>', methods=['POST'])
def make_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if payment and payment.status == 0:
        payment.status = 1  # Assuming 1 means payment is done
        db.session.commit()
        flash('Payment successful!', 'success')
    else:
        flash('Invalid payment or already processed.', 'danger')
    return redirect(url_for('show_payments'))

@app.route('/oeanalytics/sponsor/dashboard/payments/track/<int:id>', methods=['GET', 'POST'])
def make_payment_track(id):
    print(id)
    payment = Payment.query.get(id)
    payment.status = 1  # Assuming 1 means payment is done
    db.session.commit()
    # Handle GET request (if needed, otherwise you can return an error or a different page)
    flash('Paymeny Successfull', 'success')
    return redirect(url_for('show_payments_sponser'))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                      6) Influencer                   ###################


###################################################################################

@app.route('/oeanalytics/influencer/home')
def influencer_home():
    flash('Access Granted','success')
    results = db.session.query(
    Category.category,
    db.func.count(Campaign.campaignid).label('campaign_count')
    ).outerjoin(
        Campaign, 
        (Category.category == Campaign.category) & (Campaign.visibility == 'Public')
    ).group_by(
        Category.category
    ).order_by(
        db.func.trim(Category.category)
    ).all()

    return render_template("home.html",categories=results)


# 6.0 home page
@app.route('/campaigns/<category>/<filter>')
def campaigns_by_category(category,filter):
    # Query to get the campaigns that match the given category
    if filter=="all":
    
        campaigns = db.session.query(Campaign).filter_by(category=category,visibility='Public').all()

        # Return the rendered template with the campaigns
        return render_template('campaigns_by_category.html', category=category, campaigns=campaigns)
    if filter=="up":
        campaigns = db.session.query(Campaign).filter_by(
        category=category,
        visibility='Public'
        ).order_by(desc(Campaign.budget)).all()

    # Return the rendered template with the campaigns
        return render_template('campaigns_by_category.html', category=category, campaigns=campaigns)
    if filter=="down":
        campaigns = db.session.query(Campaign).filter_by(
        category=category,
        visibility='Public'
        ).order_by(Campaign.budget).all()

    # Return the rendered template with the campaigns
        return render_template('campaigns_by_category.html', category=category, campaigns=campaigns)

# 6.0.1 sending request
@app.route('/send_to_sponser/<int:campaign_id>', methods=['POST', 'GET'])
def send_to_sponser(campaign_id):
    # Retrieve the Campaign and Influencer
    campaign = Campaign.query.get_or_404(campaign_id)
    influencer = Influencer.query.filter_by(username=session['username']).first_or_404()
    # Check if the request already exists

    existing_request = Request.query.filter_by(
        influencer_u=session['username'],
        sponser_u=campaign.userid,
        campaign_id=campaign_id
    ).first()

    if existing_request:
        flash("A request for this campaign and influencer already exists.",'warning')
       # Query to get the campaigns that match the given category
        campaigns = db.session.query(Campaign).filter_by(category=campaign.category).all()
    # Return the rendered template with the campaigns
        return render_template('campaigns_by_category.html', category=campaign.category, campaigns=campaigns)
    # Create a new Request record

    new_request = Request(
        influencer_u=session['username'],
        sponser_u= campaign.userid,  # You might want to get this from the session or user context
        campaign_id=campaign_id,
        campaign_name=campaign.campaignname,
        status=0,  # Set the initial status (e.g., 0 for pending)
        payment_amount=campaign.budget,  # Set the initial payment amount (could be updated later)
        requirements=campaign.goals,  # Provide additional requirements
        messages=campaign.campaign_description,  # Provide initial messages
        role='Influencer',  # Set the role, could be "Influencer" or something else
        category = campaign.category
    )

    # Add and commit the new request to the database
    db.session.add(new_request)
    db.session.commit()

    flash(f"Request sent to {campaign.userid} for campaign '{campaign.campaignname}'.",'success')
    campaigns = db.session.query(Campaign).filter_by(category=campaign.category).all()

    # Return the rendered template with the campaigns
    return render_template('campaigns_by_category.html', category=campaign.category, campaigns=campaigns)

# 6.0.2
@app.route('/influencer_dashboard/<template>')
def influencer_dashboard(template):
    categories = Category.query.all()
    influencer = Influencer.query.all()
    return render_template('influencer_dashboard.html', template=template,categories=categories,influencers=influencer)
# 6.1 My Campaign
@app.route('/oeanalytics/influencer/dashboard/my_campaign', methods=['POST', 'GET'])
def influencer_my_campaign():
    # Retrieve the logged-in influencer's username (assuming it's available in the session)
    influencer_username = session.get('username')
    
    if not influencer_username:
        flash('User not logged in', 'danger')
        return redirect(url_for('login'))

    # Query the Request table for campaigns where the status is 1 and the influencer is the current user
    requests = Request.query.filter_by(influencer_u=influencer_username, status=1).all()
    
    # Extract campaign IDs from the filtered requests
    campaign_ids = {req.campaign_id for req in requests}
    
    # Query the Campaign table for the retrieved campaign IDs
    campaigns = Campaign.query.filter(Campaign.campaignid.in_(campaign_ids)).all()
    
    # Render the template with the list of campaigns
    return render_template('influencer_dashboard.html', template='influencer_my_campaign.html', campaigns=campaigns)

@app.route('/oeanalytics/influencer/dashboard/my_campaign/show/<int:campaignid>', methods=['POST', 'GET'])
def show_my_campaign(campaignid):
    campaign = Campaign.query.filter_by(campaignid=campaignid).first()
    return render_template('influencer_dashboard.html',template='show_campaign.html',campaign=campaign)
# 6.2 Edit Profile

# 6.2.0
@app.route('/oeanalytics/influencer/dashboard/edit_profile', methods=['POST', 'GET'])
def edit_influencer():
    user = Influencer.query.filter_by(username=session['username']).first()
    categories = Category.query.all()
    return render_template('influencer_dashboard.html',template ="edit_influencer_profile.html",user=user,categories=categories)

# 6.2.1
@app.route('/oeanalytics/influencer/dashboard/edit_profile/form', methods=['POST', 'GET'])
def edit_influencer_profile():
    print(session['username'])
    user = Influencer.query.filter_by(username=session['username']).first()
    user.password = request.form.get('password') or user.password
    user.first_name = request.form.get('first_name') or user.first_name
    user.last_name = request.form.get('last_name') or user.last_name
    user.address = request.form.get('address') or user.address
    user.district = request.form.get('district') or user.district
    user.bio = request.form.get('bio') or user.bio
    user.state = request.form.get('state') or user.state
    user.pincode = request.form.get('pincode') or user.pincode
    user.contact = request.form.get('contact') or user.contact
    user.instagram_id = request.form.get('instagram_id') or user.instagram_id
    user.linkedin_id = request.form.get('linkedin_id') or user.linkedin_id
    user.facebook_id = request.form.get('facebook_id') or user.facebook_id
    user.x_id = request.form.get('x_id') or user.x_id
    user.category = request.form.get('category') or user.category
    user.insta_f = request.form.get('insta_f') or user.insta_f
    user.linkedin_f = request.form.get('linkedin_f') or user.linkedin_f
    user.facebook_f = request.form.get('facebook_f') or user.facebook_f 
    user.x_f = request.form.get('x_f') or user.x_f
    db.session.commit()
    flash('profile edited Sucessfully','success')
    results = db.session.query(
            Category.category,
            db.func.count(Campaign.campaignid).label('campaign_count')
            ).outerjoin(Campaign, Category.category == Campaign.category) \
            .group_by(Category.category) \
            .order_by(db.func.trim(Category.category)) \
            .all()

    return redirect(url_for('edit_influencer'))
# 6.3 Incoming Ad Request
@app.route('/oeanalytics/influencer/dashboard/incoming/<filter>', methods=['POST', 'GET'])
def incoming_influencer(filter):
    if filter == 'All':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Sponser').all()
        return render_template('influencer_dashboard.html',template='incoming_influencer.html',requests = requests)
    if filter == 'Not Responded':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Sponser',status=0).all()
        return render_template('influencer_dashboard.html',template='incoming_influencer.html',requests = requests)
    if filter == 'Accepted':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Sponser',status=1).all()
        return render_template('influencer_dashboard.html',template='incoming_influencer.html',requests = requests)
    if filter == 'Rejected':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Sponser',status=2).all()
        return render_template('influencer_dashboard.html',template='incoming_influencer.html',requests = requests)

# 6.3.0
@app.route('/oeanalytics/influencer/dashboard/incoming/update/<int:request_id>/<int:new_status>', methods=['POST', 'GET'])
def update_request_influencer(request_id, new_status):
    request = Request.query.get(request_id)
    request.status = new_status
    db.session.commit()
    if new_status == 1:
        campaign = Campaign.query.get(request.campaign_id)
        campaign.alloted = 1
        db.session.commit()
        # Get the campaign_id from the updated request
        campaign_id = request.campaign_id

        # Step 3: Find other requests with the same campaign_id and status 0
        other_requests = Request.query.filter(
            Request.campaign_id == campaign_id,
            Request.status == 0
        ).all()

        # Step 4: Update these requests to status 3 (Ad Closed)
        for req in other_requests:
            req.status = 3
        db.session.commit()
        payment = Payment(
            influencer_u=session['username'],
            sponser_u=request.sponser_u,  # Assuming the sponsor's username is stored in the session
            campaign_id=campaign_id,
            amount=request.payment_amount,  # Assuming amount is part of the Request model or you need to define it
            status=0,  # Assuming initial status for the payment (e.g., 0 for pending)
            campaign_name=campaign.campaignname  # Assuming the campaign name is part of the Campaign model
        )
        db.session.add(payment)
        db.session.commit()
        flash('Accepted','success')
    requests = Request.query.filter_by(sponser_u=session['username'],role='Sponser').all()
    return redirect(url_for('incoming_influencer',filter='All'))

# 6.4 Outgoing Ad Request
@app.route('/oeanalytics/influencer/dashboard/outgoing/<filter>', methods=['POST', 'GET'])
def outgoing_influencer(filter):
    if filter == 'All':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer').all()
        return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)
    if filter == 'Not Responded':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer',status=0).all()
        return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)
    if filter == 'Accepted':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer',status=1).all()
        return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)
    if filter == 'Rejected':
        requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer',status=2).all()
        return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)

# 6.4.1
@app.route('/oeanalytics/influencer/dashboard/outgoing/delete/<int:request_id>', methods=['POST', 'GET'])
def delete_request_influencer(request_id):
    # Query the request by ID
    request_to_delete = Request.query.get(request_id)
    db.session.delete(request_to_delete)
    db.session.commit()
    flash('Request deleted successfully!', 'success')
    requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer',status=0).all()
    return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)

# 6.4.2
@app.route('/oeanalytics/influencer/dashboard/outgoing/edit/<int:request_id>', methods=['POST', 'GET'])
def edit_page_influencer(request_id):
    requests = Request.query.get(request_id)
    return render_template('influencer_dashboard.html',template ='edit_request_influencer.html',requests =requests )

# 6.4.2.1
@app.route('/edit_request_influencer/<int:request_id>', methods=['POST', 'GET'])
def edit_request_influencer(request_id):
    requests = Request.query.get(request_id)
    requests.requirements = request.form.get('Requirements') or requests.requirements
    requests.messages = request.form.get('Message') or requests.messages
    requests.payment_amount = request.form.get('Amount') or requests.payment_amount
    db.session.commit()
    flash('edit request done successfully', 'success')
    requests = Request.query.filter_by(influencer_u=session['username'],role='Influencer').all()
    return render_template('influencer_dashboard.html',template='outgoing_influencer.html',requests = requests)

#6.5
@app.route('/oeanalytics/influencer/dashboard/payments')
def show_payments_influencer():
    # Retrieve influencer username from the session (or however you store it)
    influencer_username = session.get('username')  # Adjust this if you store it differently

    # Filter payments by influencer username
    payments = Payment.query.filter_by(influencer_u=influencer_username).all()
    
    return render_template('influencer_dashboard.html', template='payment_influencer.html', payments=payments)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


###################################################################################


##########                        7) Admin                 ########################


###################################################################################


@app.route('/oeanalytics/admin/dashboard/', methods=['POST', 'GET'])
def admin_home():
    return render_template('admin_dashboard.html',template='template.html')

# 7.0 Admin func
@app.route('/oeanalytics/admin/dashboard/<template>', methods=['POST', 'GET'])
def adminfunc(template):
    categories = Category.query.all()
    return render_template('admin_dashboard.html', template=template,categories=categories)

# 7.1 Add Category
@app.route('/oeanalytics/admin/dashboard/add_category', methods=['POST', 'GET'])
def add_category():
    if request.method == 'POST':
        # Get form data
        category_name = request.form['category']
        description = request.form['description']
        # Save current date and time
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_category = Category(category=category_name, 
                                description=description, date=date)
        db.session.add(new_category)
        db.session.commit()
        flash('Category added successfully','success')
        return redirect(url_for('adminfunc',template='addcategory.html'))

# 7.2 Edit Category
@app.route('/oeanalytics/admin/dashboard/edit/category/page/<category>', methods=['POST', 'GET'])
def edit_cat_page(category):
    categories = Category.query.filter_by(category=category).first()
    return render_template('admin_dashboard.html', template='editcategory.html',category=categories)
    
# Function 
@app.route('/oeanalytics/admin/dashboard/edit/category/<category>', methods=['POST', 'GET'])
def edit_cat(category):
    categories = Category.query.filter_by(category=category).first()
    categories.category = request.form['category'] or categories.category
    categories.description = request.form['description'] or categories.description
        # Save current date and time
    db.session.commit()
    categorie = Category.query.all()
    flash('category updated succesfully','success')
    return redirect(url_for('adminfunc', template='category.html'))
# 7.3 Category List

# maganged by adminfunc

# 7.4 Influencer List
# 7.4.0

@app.route('/oeanalytics/admin/dashboard/influencer/<column>', methods=['POST', 'GET'])
def filter(column):
    # Ensure the column_name is valid
    if not hasattr(Influencer, column):
        influencers = Influencer.query.all()
        flash(f"Column {column} does not exist in the Influencer table.",'danger')
        return render_template('admin_dashboard.html',template ='admin_influencer.html',influencers=influencers)
    # Get the column object
    column = getattr(Influencer, column)
    # Query the database and sort by the specified column
    influencer = db.session.query(Influencer).order_by(column).all()
    return render_template('admin_dashboard.html',template ='admin_influencer.html',influencers=influencer)

# 7.4.8 delete button
@app.route('/oeanalytics/admin/dashboard/influencer/delete/<username>', methods=['POST', 'GET'])
def admin_influencer_delete(username):
    influencer = Influencer.query.get(username)
    if not influencer:
        flash('Influencer not found.', 'warning')
        return redirect(url_for('filter', column='username'))

    # Delete related records in Request table
    Request.query.filter(Request.influencer_u == username).delete()

    # Now delete the influencer
    db.session.delete(influencer)
    db.session.commit()

    return redirect(url_for('filter',column='username'))

# 7.4.9 flag button
@app.route('/admin_dashboard/influencer/flag/<string:id>/<int:flag>', methods=['POST', 'GET'])
def admin_influencer_flag(id, flag):
    # Fetch the influencer by id
    influencer = Influencer.query.get(id)
    
    if influencer is None:
        flash('Influencer not found.', 'warning')
        return redirect(url_for('filter', column='username'))

    # Update the flag status
    influencer.flag = flag
    db.session.commit()

    # Update requests based on flag value
    if flag == 1:
        # Find requests with status 0 for the influencer
        other_requests = Request.query.filter(
            Request.influencer_u == id,
            Request.status == 0
        ).all()

        # Update these requests to status 5 (Ad Closed)
        for req in other_requests:
            req.status = 5
    
    elif flag == 0:
        # Find requests with status 5 for the influencer
        other_requests = Request.query.filter(
            Request.influencer_u == id,
            Request.status == 5
        ).all()

        # Update these requests to status 0 (Open)
        for req in other_requests:
            req.status = 0
    
    # Commit the changes
    db.session.commit()

    # Fetch updated influencer list
    influencers = Influencer.query.all()
    return redirect(url_for('filter',column='username'))

# 7.5 Sponser list
# 7.5.0

@app.route('/oeanalytics/admin/dashboard/sponser/<column>', methods=['POST', 'GET'])
def filter_sponser(column):
    if not hasattr(Sponsor, column):
        flash(f"Column {column} does not exist in the Campaign table.",'danger')
        sponsers = Sponsor.query.all()
        return render_template('admin_dashboard.html',template ='admin_sponser.html',sponsers=sponsers)
    # Get the column object
    column = getattr(Sponsor, column)
    # Query the database and sort by the specified column
    sorted_sponsors = db.session.query(Sponsor).order_by(column).all()
    return render_template('admin_dashboard.html',template ='admin_sponser.html',sponsers=sorted_sponsors)

# 7.5.1 delte button
@app.route('/oeanalytics/admin/dashboard/sponser/delete/<username>', methods=['POST', 'GET'])
def admin_sponser_delete(username):
    sponsor = Sponsor.query.get(username)
    if not sponsor:
        flash('Sponsor not found.', 'warning')
        return redirect(url_for('filter_sponser',column='username'))

    # Delete related records in Request table
    Request.query.filter(Request.sponser_u == username).delete()

    # Delete related records in Campaign table
    Campaign.query.filter(Campaign.userid == username).delete()

    # Now delete the sponsor
    db.session.delete(sponsor)
    db.session.commit()
    flash('Deleted', 'danger')
    return redirect(url_for('filter_sponser',column='username'))

# 7.5.2 flag button
@app.route('/oeanalytics/admin/dashboard/sponsor/flag/<string:id>/<int:flag>', methods=['POST', 'GET'])
def admin_sponsor_flag(id, flag):
    # Fetch the sponsor by id
    sponsor = Sponsor.query.get(id)
    
    if sponsor is None:
        flash('Sponsor not found.', 'warning')
        return redirect(url_for('filter_sponser', column='username'))

    # Fetch the campaign associated with the sponsor
    campaign = Campaign.query.filter_by(userid=id).first()
    
    if campaign:
        campaign.flag = flag
    
    sponsor.flag = flag
    db.session.commit()

    if flag == 1:
        # Update requests with status 0 for the sponsor
        other_requests = Request.query.filter(
            Request.sponser_u == id,
            Request.status == 0
        ).all()

        # Update these requests to status 6 (Ad Closed)
        for req in other_requests:
            req.status = 6
    
    elif flag == 0:
        # Update requests with status 6 for the sponsor
        other_requests = Request.query.filter(
            Request.sponser_u == id,
            Request.status == 6
        ).all()

        # Update these requests to status 0 (Open)
        for req in other_requests:
            req.status = 0

    # Commit changes after all updates
    db.session.commit()

    # Fetch updated sponsor list
    sponsors = Sponsor.query.all()
    return redirect(url_for('filter_sponser',column='username'))

# 7.6 Campaign list

# 7.6.0
@app.route('/oeanalytics/admin/dashboard/campaign/<column>', methods=['POST', 'GET'])
def filter_campaigns(column):
    # Ensure the column_name is valid
    if not hasattr(Campaign, column):
        flash(f"Column {column} does not exist in the Campaign table.",'danger')
        cammpaign = Campaign.query.all()
        return render_template('admin_dashboard.html',template ='admin_campaign.html',campaigns=cammpaign)
    column = getattr(Campaign, column)
    
    # Query the database and sort by the specified column
    sorted_campaigns = db.session.query(Campaign).order_by(column).all()
    return render_template('admin_dashboard.html',template ='admin_campaign.html',campaigns=sorted_campaigns)

# 7.6.1
@app.route('/admin_dashboard/campaign_delete/<int:campaign_id>', methods=['POST', 'GET'])
def admin_campaign_delete(campaign_id):
    # Retrieve the campaign using the campaign_id parameter
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        flash('Campaign not found.', 'warning')
        return redirect(url_for('filter_campaigns', column='campaignid'))

    # Delete related records in the Request table
    Request.query.filter(Request.campaign_id == campaign_id).delete()

    # Now delete the campaign
    db.session.delete(campaign)
    db.session.commit()

    return redirect(url_for('filter_campaigns', column='campaignid'))

# 7.6.2
@app.route('/oeanalytics/admin/dashboard/campaign/flag/<int:id>/<int:flag>', methods=['POST', 'GET'])
def admin_campaign_flag(id, flag):
    # Fetch the campaign by id
    campaign = Campaign.query.get(id)
    
    if campaign is None:
        flash('Campaign not found.', 'warning')
        return redirect(url_for('filter_campaign', column='campaignid'))

    # Update campaign flag
    campaign.flag = flag
    db.session.commit()

    # Update requests based on the flag status
    if flag == 1:
        # Find requests with the same campaign_id and status 0
        other_requests = Request.query.filter(
            Request.campaign_id == campaign.campaignid,
            Request.status == 0
        ).all()

        # Update these requests to status 4 (Ad Closed)
        for req in other_requests:
            req.status = 4

    elif flag == 0:
        # Find requests with the same campaign_id and status 4
        other_requests = Request.query.filter(
            Request.campaign_id == campaign.campaignid,
            Request.status == 4
        ).all()

        # Update these requests to status 0 (Open)
        for req in other_requests:
            req.status = 0

    # Commit changes after all updates
    db.session.commit()

    # Fetch updated campaign list
    campaigns = Campaign.query.all()
    return redirect(url_for('filter_campaigns',column='campaignid'))


# 7.7 Request

@app.route('/oeanalytics/admin/dashboard/request/<column>', methods=['POST', 'GET'])
def filter_request(column):
    # Ensure the column_name is valid
    if not hasattr(Request, column):
        flash(f"Column {column} does not exist in the Request table.",'danger')
        requests = Request.query.all()
        return render_template('admin_dashboard.html',template ='admin_request.html',requests=requests)
    
    # Get the column object
    column = getattr(Request, column)
    
    # Query the database and sort by the specified column
    sorted_requests = db.session.query(Request).order_by(column).all()
    
    return render_template('admin_dashboard.html',template ='admin_request.html',requests=sorted_requests)


# 7.7.1
@app.route('/admin_dashboard/request_delete/<int:request_id>', methods=['POST', 'GET'])
def admin_request_delete(request_id):
    request_to_delete = Request.query.get(request_id)
    db.session.delete(request_to_delete)
    db.session.commit()
    requests = Request.query.all()
    return render_template('admin_dashboard.html',template ='admin_request.html',requests=requests)

# 7.8 payments
@app.route('/oeanalytics/admin/dashboard/payments/<column>', methods=['POST', 'GET'])
def filter_payments(column):
    # Ensure the column_name is valid
    if not hasattr(Payment, column):
        flash(f"Column {column} does not exist in the Payment table.",'danger')
        payments = Payment.query.all()
        return render_template('admin_dashboard.html',template ='payment_admin.html',payments= payments)
    # Get the column object
    column = getattr(Payment, column)
    
    # Query the database and sort by the specified column
    sorted_payments = db.session.query(Payment).order_by(column).all()
    
    return render_template('admin_dashboard.html',template ='payment_admin.html',payments= sorted_payments)

@app.route('/oeanalytics/admin/dashboard/statistics',methods=['POST', 'GET'])
def statistics():
    # Count the number of entries in each table
    admin_count = db.session.query(func.count(Admin.user_id)).scalar()
    campaign_count = db.session.query(func.count(Campaign.campaignid)).scalar()
    category_count = db.session.query(func.count(Category.category)).scalar()
    influencer_count = db.session.query(func.count(Influencer.username)).scalar()
    payment_count = db.session.query(func.count(Payment.id)).scalar()
    request_count = db.session.query(func.count(Request.request_id)).scalar()
    sponsor_count = db.session.query(func.count(Sponsor.username)).scalar()

    # Count the number of requests by status
    request_status_counts = db.session.query(Request.status, func.count(Request.request_id)).group_by(Request.status).all()
    request_status_dict = {status: count for status, count in request_status_counts}

    # Count the number of payments by status
    payment_status_counts = db.session.query(Payment.status, func.count(Payment.id)).group_by(Payment.status).all()
    payment_status_dict = {status: count for status, count in payment_status_counts}

    return render_template('admin_dashboard.html',template='statistics.html', 
                           admin_count=admin_count, 
                           campaign_count=campaign_count,
                           category_count=category_count,
                           influencer_count=influencer_count,
                           payment_count=payment_count,
                           request_count=request_count,
                           sponsor_count=sponsor_count,
                           request_status_dict=request_status_dict,
                           payment_status_dict=payment_status_dict)



if __name__ == '__main__':
    app.run(debug=True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
