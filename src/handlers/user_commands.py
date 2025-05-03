import os
from create_bot import data_dir, benefit_types
from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile
from client.get_messages import get_message
from keyboards.reply_kb.start_kb import start_keyboard
from keyboards.inline_kb.benefits_types import create_benefits_types_kb, create_benefit_type_back
from keyboards.inline_kb.benefits_subtypes import create_benefits_some_type_kb, create_benefits_subtype_kb

router = Router()

class Benefit(StatesGroup): #Хранят в себе callback значения (нужно для обработки кнопки Назад)
    state_1 = State()
    state_2 = State()
    state_3 = State()
    state_4 = State()

@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(await get_message('start_message'),
                         reply_markup=start_keyboard())

@router.message(F.text.lower() == 'файл с льготами')
async def get_file_beneftis(message: Message):
    document_file = FSInputFile(path=os.path.join(data_dir, 'Льготы.pdf'))
    await message.answer_document(document=document_file, caption= await get_message('file_benefits'))
    
@router.message(F.text.lower() == 'льготы')
async def get_list_benefits(message: Message, state: FSMContext):
    await state.set_state(Benefit.state_1.state)
    await state.update_data(state_1='list_benefits')
    await message.answer(await get_message('list_benefits'), 
                         reply_markup=create_benefits_types_kb())

@router.callback_query(Benefit.state_1, F.data.startswith('list_type_benefits_'))
async def get_benefits_type(call: CallbackQuery, state: FSMContext):
    await state.set_state(Benefit.state_2.state)
    await state.update_data(state_2=call.data)
    await call.message.edit_text(await get_message(call.data), 
                                reply_markup=create_benefits_some_type_kb(benefit_types[call.data]))
    
@router.callback_query(Benefit.state_2, F.data.startswith('benefit_name_'))
async def get_benefit_type(call: CallbackQuery, state: FSMContext):
    await state.set_state(Benefit.state_3.state)
    await state.update_data(state_3=call.data)
    await call.message.edit_text(await get_message(call.data),
                              reply_markup=create_benefits_subtype_kb(call.data))

@router.callback_query(Benefit.state_3, F.data.startswith('benefit_name_'))
async def get_benefit_type_content_or_acts(call: CallbackQuery, state: FSMContext):
    await state.set_state(Benefit.state_4.state)
    await state.update_data(state_4=call.data)
    await call.message.edit_text(await get_message(call.data),
                              reply_markup=create_benefit_type_back(), disable_web_page_preview=True)
    
@router.callback_query(StateFilter('*'), F.data == "back")
async def back_handler(call: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    data = await state.get_data()

    if current_state == Benefit.state_2.state:
        await call.message.edit_text(
            await get_message('list_benefits'),
            reply_markup=create_benefits_types_kb()
        )
        await state.set_state(Benefit.state_1.state)
        
    elif current_state == Benefit.state_3.state:
        call_data = data.get('state_2')
        await call.message.edit_text(
            await get_message(call_data),
            reply_markup=create_benefits_some_type_kb(benefit_types[call_data])
        )
        await state.set_state(Benefit.state_2.state)
        
    elif current_state == Benefit.state_4.state:
        call_data = data.get('state_3')  
        await call.message.edit_text(
            await get_message(call_data),
            reply_markup=create_benefits_subtype_kb(call_data)
        )
        await state.set_state(Benefit.state_3.state) 
    