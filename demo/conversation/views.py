from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from items.models import Item
from .forms import ConversationMessage
from .models import Conversation

@login_required
def new_conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)

    if item.created_by==request.user:
        return redirect('dashboard:index')

    conversation=Conversation.objects.filter(item=item).filter(members=request.user)

    if conversation:
        return redirect('conversation:detail', pk=conversation.first().pk)
    
    if request.method=='POST':
        form=ConversationMessage(request.POST)

        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            return redirect('item:detail',pk=item_pk)
    else:
        form=ConversationMessage()
    
    return render(request,'conversation/new.html',{
        'form':form
    })
@login_required
def inbox(request):
    conversation=Conversation.objects.filter(members=request.user)
    return render(request,'conversation/inbox.html',{
        'conversations':conversation
    })




            

