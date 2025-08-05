# 🍗 KFC Live Agent - Cloud Run Deployment Guide

This guide will help you deploy your KFC Live Agent to Google Cloud Run in just a few steps.

## 📋 Prerequisites

1. **Google Cloud CLI installed**
   ```bash
   # Install gcloud CLI (if not already installed)
   # Visit: https://cloud.google.com/sdk/docs/install
   ```

2. **Google Cloud Project**
   - You'll be prompted to create one during deployment if needed
   - Or use an existing project

3. **Environment Variables**
   - Your `.env` file with `GOOGLE_API_KEY`

## 🚀 Quick Deployment

### 1. One-Command Deployment
```bash
./deploy.sh
```

That's it! The script will:
- ✅ Check your `.env` file and load environment variables
- ✅ Validate your Google API key
- ✅ Authenticate with Google Cloud (if needed)
- ✅ Set up your project (if needed)
- ✅ Enable required APIs
- ✅ Deploy to Cloud Run with optimal settings

### 2. Manual Deployment (Alternative)

If you prefer manual control:

```bash
# Authenticate
gcloud auth login

# Set project
gcloud config set project YOUR-PROJECT-ID

# Enable APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

# Deploy
gcloud run deploy kfc-live-agent \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY="YOUR_API_KEY_HERE" \
  --memory 2Gi \
  --cpu 2 \
  --timeout 3600 \
  --max-instances 10
```

## 📁 Deployment Files

The following files are configured for Cloud Run:

- **`Dockerfile`** - Container configuration for Python 3.11
- **`.gcloudignore`** - Excludes sensitive files from deployment
- **`deploy.sh`** - Automated deployment script
- **`app/main.py`** - Updated to handle Cloud Run PORT environment variable

## ⚙️ Configuration Details

### Cloud Run Settings
- **Service Name**: `kfc-live-agent`
- **Region**: `us-central1`
- **Memory**: `2Gi`
- **CPU**: `2`
- **Max Instances**: `10`
- **Timeout**: `3600 seconds` (1 hour)
- **Port**: `8080`
- **Access**: Public (no authentication required)

### Environment Variables
- **`GOOGLE_API_KEY`** - Automatically set from your `.env` file
- **`PORT`** - Automatically set by Cloud Run (8080)

## 🔒 Security Features

✅ **API Key Protection**: Never exposed in command history or logs
✅ **File Exclusion**: `.env` files excluded from deployment via `.gcloudignore`
✅ **Secure Environment**: Variables set directly in Cloud Run
✅ **No Local Secrets**: Production deployment contains no sensitive data

## 📱 Features Available After Deployment

Your deployed KFC Live Agent will include:

- 🍗 **Real-time KFC Assistant** in Spanish
- 🎤 **Voice Interaction** with Spanish audio processing
- 🥤 **Interactive KFC Menu** with MDK Wednesday specials
- 🛒 **Live Order Tracking** with real-time updates
- 📱 **Mobile-Responsive Design** with KFC branding
- ⚡ **WebSocket Support** for instant communication
- 🔄 **Auto-scaling** from 0 to 10 instances based on traffic

## 🌐 After Deployment

Once deployed, you'll get a URL like:
```
https://kfc-live-agent-xxxxxxxxx-uc.a.run.app
```

### Testing Your Deployment
1. Open the URL in your browser
2. You should see the KFC interface with:
   - KFC branding and colors
   - Three-column layout (Menu | Chat | Order)
   - Interactive menu items
3. Try chatting: "Hola" or "Quiero MDK 6 piezas combo"
4. Test voice functionality (microphone button)

### Monitoring
- **Cloud Run Console**: Check logs and metrics
- **Debug Endpoints**:
  - `/debug/pedidos` - View active orders
  - `/debug/menu` - View KFC menu structure
  - `/api/pedido/default` - Check order API

## 💰 Cost Optimization

Cloud Run pricing is pay-per-use:
- **Scales to zero** when not in use = $0 cost during idle time
- **Only pay for actual requests** and processing time
- **Estimated cost**: Very low for moderate usage (typically <$10/month)

## 🔧 Troubleshooting

### Common Issues

1. **Authentication Error**
   ```bash
   gcloud auth login
   gcloud config set project YOUR-PROJECT-ID
   ```

2. **API Key Error**
   - Check your `.env` file contains `GOOGLE_API_KEY=your_key_here`
   - Ensure no extra spaces or quotes

3. **Deployment Timeout**
   - Wait for build to complete (can take 5-10 minutes first time)
   - Check Cloud Build logs in Google Cloud Console

4. **502 Bad Gateway**
   - Check Cloud Run logs for startup errors
   - Verify all dependencies in `requirements.txt`

### Getting Help

- **Cloud Run Logs**: `gcloud run logs tail kfc-live-agent --region us-central1`
- **Service Status**: Check Google Cloud Run console
- **Local Testing**: Run `cd app && uvicorn main:app --reload` first

## 🔄 Updates and Redeployment

To update your deployed service:
```bash
# Make your changes, then redeploy
./deploy.sh
```

The script will automatically:
- Build a new container image
- Deploy the updated version
- Maintain zero downtime during deployment

---

🎉 **Congratulations!** Your KFC Live Agent is now running on Google Cloud Run with enterprise-grade scalability and reliability!
