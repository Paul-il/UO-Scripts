Program AutoLumber_SW;

{$Include 'all.inc'}

const
/////////////////////////////////////////////////
// Обязательные к изменению настройки скрипта  //
//                                             //
// Координаты точки перед сундуком             //
// Occlo:                                       //
xTileSunduk = 2850;                            //
yTileSunduk = 175;                             //
//                                             //
/////////////////////////////////////////////////

// Возможные к изменению настройки скрипта
MyMaxWeight = 100;// Максимальный вес
Hatchet = $0F43;   // Тип топора
UseArms = 1;
Sunduk = $53D5136B;

// Размерности массивов
iTTileCount = 40;   // Типы тайлов деревьев (менять, только при редактировании массива)
iCTileCount = 3;    // Кол-во точек (центров поляны), в которых хотим собирать информацию о деревьях (поляна = 30х30 тайлов)

// Журнал
Msg1 = 'You stop lumberjacking.';
Msg2 = 'That is too far away';
Msg3 = 'hack';
Msg4 = 'You decide not to chop wood';
Msg5 = 'no wood here to chop...';
Msg6 = 'appears immune';
Msg7 = 'wood left';
Msg8 = 'reach this';
Msg9 = 'tool breaks';

// Прочее
RunSpeed = 250;
iRadiusSearch = 12; // Радиус (не диаметр!) поиска деревьев в тайлах, относительно персонажа
Logs = $1BDD;       // Тип логов
WoodType = $0F90;   // Тип дедвудов

type
ChopTile = Record
x, y : Integer;
end;

var
Regs : array [1..3] of Cardinal;
FoundTilesArray : TFoundTilesArray;
TempFoundTilesArray, ChopTilesArray : array of TFoundTile;
TreeTile:array [0..iTTileCount] of word;
ChopTiles : array[1..iCTileCount] of ChopTile;
ctime : TDateTime;
i : Integer;
n: TDateTime;

// Инициализация массива типов тайлов деревьев
procedure InitTTilesArray;
begin

  TreeTile[0]:=3274;
  TreeTile[1]:=3275;
  TreeTile[2]:=3277;
  TreeTile[3]:=3280;


  TreeTile[4]:=3283;
  TreeTile[5]:=3286;
  TreeTile[6]:=3288;
  TreeTile[7]:=3290;


  TreeTile[8]:=3293;
  TreeTile[9]:=3296;
  TreeTile[10]:=3299;
  TreeTile[11]:=3302;


  TreeTile[12]:=3320;
  TreeTile[13]:=3323;
  TreeTile[14]:=3326;
  TreeTile[15]:=3329;


  TreeTile[16]:=3393;
  TreeTile[17]:=3394;
  TreeTile[18]:=3395;
  TreeTile[19]:=3396;


  TreeTile[20]:=3415;
  TreeTile[21]:=3416;
  TreeTile[22]:=3417;
  TreeTile[23]:=3418;


  TreeTile[24]:=3419;
  TreeTile[25]:=3438;
  TreeTile[26]:=3439;
  TreeTile[27]:=3440;


  TreeTile[28]:=3441;
  TreeTile[29]:=3442;
  TreeTile[30]:=3460;
  TreeTile[31]:=3461;


  TreeTile[32]:=3462;
  TreeTile[33]:=3476;
  TreeTile[34]:=3478;
  TreeTile[35]:=3480;


  TreeTile[36]:=3482;
  TreeTile[37]:=3484;
  TreeTile[38]:=3492;
  TreeTile[39]:=3496;
end;

// Инициализация массива координат для поиска деревьев
procedure InitCTilesArrayFirst;
begin
  ChopTiles[1].x := 3568;
  ChopTiles[1].y := 2545;

  ChopTiles[2].x := 3545;
  ChopTiles[2].y := 2551;
  
  ChopTiles[3].x := 3526;
  ChopTiles[3].y := 2551;
end;

// Инициализация системных переменных
procedure InitSystem;
begin
  SetRunUnmountTimer(RunSpeed);
  SetArrayLength(ChopTilesArray, 1);
end;

// Инициализация регов
procedure InitReg;
begin
  Regs[1] := $0F85;      // Ginseng
  Regs[2] := $0F88;      // Nightshade
  Regs[3] := $0F86;      // Mandrake Roots
end;

// Поиск деревьев
procedure SearchTree;
var
i, j : Integer;
iFoundTilesArrayCount : word;
iTempFoundTilesArrayCount : Integer;

begin
  for i:= 0 to iTTileCount do
  begin
    iFoundTilesArrayCount := GetStaticTilesArray((GetX(Self) - iRadiusSearch), (GetY(Self) - iRadiusSearch), (GetX(Self) + iRadiusSearch), (GetY(Self) + iRadiusSearch), 1, TreeTile[i], FoundTilesArray);
    if iFoundTilesArrayCount > 0 then
    begin
      SetArrayLength(TempFoundTilesArray, Length(TempFoundTilesArray) + iFoundTilesArrayCount);
      for j := 0 to iFoundTilesArrayCount - 1 do
      begin
        TempFoundTilesArray[iTempFoundTilesArrayCount + j] := FoundTilesArray[j];
      end;
      iTempFoundTilesArrayCount := iTempFoundTilesArrayCount + iFoundTilesArrayCount;
    end;
  end;
  AddToSystemJournal('Найдено деревьев: ' + IntToStr(iTempFoundTilesArrayCount));
end;

// Чистим записи дубликаты (Vizit0r :P)
procedure ClearDuplicate;
var
i, j : Integer;

begin
  ChopTilesArray[Length(ChopTilesArray) - 1] := TempFoundTilesArray[0];
  for i:=1 to Length(TempFoundTilesArray) - 1 do
  begin
    for j:=0 to Length(ChopTilesArray) - 1 do
    if (ChopTilesArray[j] = TempFoundTilesArray[i]) then
    break;
    if j > Length(ChopTilesArray) - 1 then
    begin
      SetArrayLength(ChopTilesArray, Length(ChopTilesArray) + 1);
      ChopTilesArray[Length(ChopTilesArray) - 1] := TempFoundTilesArray[i];
    end;
  end;
  AddToSystemJournal('После отсеивания дубликатов, осталось деревьев:' + IntToStr(Length(ChopTilesArray)));
end;

// Возводим в степень 2 (Shinma)
function sqr(a:LongInt):LongInt;
begin
  result:=a*a;
end;

// Вычисляем длину вектора (Shinma)
function vector_length(c_2:TFoundTile):LongInt;
begin
  result:=Round(sqrt(sqr(GetX(self)-c_2.X)+sqr(GetY(self)-c_2.Y)));
end;

// «Быстрая сортировка» по длине вектора, от центра последней поляны ко всем собранным координатам деревьев
procedure QuickSort(A: array of TFoundTile; l,r: integer);
var
i, j: Integer;
x, y: TFoundTile;

begin
  i := l;
  j := r;
  x := A[((l + r) div 2)];
  repeat
    while vector_length(A[i]) < vector_length(x) do inc(i);
    while vector_length(x) < vector_length(A[j]) do dec(j);
    if not (i>j) then
    begin
      y:= A[i];
      A[i]:= A[j];
      A[j]:= y;
      inc(i);
      dec(j);
    end;
  until i>j;
  if l < j then QuickSort(ChopTilesArray, l,j);
  if i < r then QuickSort(ChopTilesArray, i,r);
end;

// Находим, исключаем дубликаты, сортируем деревья
procedure MarkTrees;
begin
  for i:= 1 to iCTileCount do
  begin
    NewMoveXY(ChopTiles[i].x, ChopTiles[i].y, False, 1, False);
    SearchTree;
    AddToSystemJournal('Всего найдено деревьев: ' + IntToStr(Length(TempFoundTilesArray)));
    ClearDuplicate;
  end;
  QuickSort(ChopTilesArray, 0, Length(ChopTilesArray) - 1);
end;

// Разгрузка (Edred)
procedure Discharge;
// разгружаем нарубленное в сундук
// нарубленное - реги в массиве Regs[1..3]
// логи - константа Logs
var
m : integer;
tmpid, tmpstack, tmpcolor : Cardinal;
tmpname : String;
begin
  AddToSystemJournal('Разгружаемся');
  waitconnection(3000);
  //UOSay('banka');
  UseObject(Sunduk);
  wait(1000);
  checksave;
  // выложим реги
  for m := 1 to 3 do
  begin
    Repeat
      tmpid := Findtype(Regs[m],backpack);
      if tmpid = 0 then break;
      addtosystemjournal( 'Найдено ' + inttostr(GetQuantity(tmpid)) + ' regs');
      MoveItem(tmpid,GetQuantity(tmpid),Sunduk,0,0,0);
      wait(1000);
      CheckSave;
    until tmpid = 0;
  end;
  // выложим дид вуды
  Repeat
    tmpid := Findtype(WoodType,backpack);
    if tmpid = 0 then break;
    addtosystemjournal( 'Найдено ' + inttostr(GetQuantity(tmpid)) + ' dead woods');
    tmpstack := Findtype(WoodType,Sunduk);
    // Если не найден в банке - тогда просто в контейнер
    if tmpstack = 0 then tmpstack := Sunduk;
    MoveItem(tmpid,GetQuantity(tmpid),tmpstack,0,0,0);
    wait(1000);
    CheckSave;
  until tmpid = 0;
  // выложим логи
  Repeat
    tmpid := Findtype(Logs,backpack);
    if tmpid = 0 then break;
    tmpcolor := GetColor(tmpid);
    tmpname := ' unknown logs';
    case tmpcolor of
      $0000 : tmpname := ' logs';
      $0505 : tmpname := ' Birch logs ';
      $0654 : tmpname := ' Cherry logs ';
      $048A : tmpname := ' Swamp logs ';
      $0415 : tmpname := ' Oak logs ';
      $0203 : tmpname := ' Hardranger logs ';
      $0487 : tmpname := ' Jade logs ';
      $0654 : tmpname := ' Cherry logs';
      $0542 : tmpname := ' Stormteal logs';
      $0489 : tmpname := ' Blizzard logs';
      $066D : tmpname := ' Vulcanic logs';
      $0492 : tmpname := ' Vampiric logs';
      $0488 : tmpname := ' Zulu logs';
      $0485 : tmpname := ' Darkness logs';
      $0498 : tmpname := ' Elven logs';
    end;
    addtosystemjournal( 'Найдено ' + inttostr(GetQuantity(tmpid)) + tmpname);
    repeat
      tmpstack := FindtypeEx(Logs,tmpcolor,Sunduk,False);
      if GetQuantity(tmpstack) >= 1500 then Ignore(tmpstack);
    until (tmpstack = 0) OR (GetQuantity(tmpstack) < 1500);
    // Если не найден в сундуке - тогда просто в контейнер
    if tmpstack = 0 then tmpstack := Sunduk;
    MoveItem(tmpid,GetQuantity(tmpid),tmpstack,0,0,0);
    wait(1000);
    CheckSave;
  until tmpid = 0;
  IgnoreReset;
  hungry(1,sunduk);
  AddToSystemJournal('Разгрузка закончена');
  AddToSystemJournal('Logs:'+IntToStr(CountEx($1BDD,$0000,Sunduk))+' '+'Birch:'+IntToStr(CountEx($1BDD,$0505,Sunduk))+' '+'Cherry:'+IntToStr(CountEx($1BDD,$0654,Sunduk))+' '+'Swamp:'+IntToStr(CountEx($1BDD,$048A,Sunduk))+' '+'Oak:'+IntToStr(CountEx($1BDD,$0415,Sunduk))+' '+'Hardranger:'+IntToStr(CountEx($1BDD,$0203,Sunduk))+' '+'Jade:'+IntToStr(CountEx($1BDD,$0487,Sunduk))+' '+'Stormteal:'+IntToStr(CountEx($1BDD,$0542,Sunduk))+' '+'Blizzard:'+IntToStr(CountEx($1BDD,$0489,Sunduk))+' '+'Vulcanic:'+IntToStr(CountEx($1BDD,$066D,Sunduk))+' '+'Vampiric:'+IntToStr(CountEx($1BDD,$0492,Sunduk))+' '+' Zulu:'+IntToStr(CountEx($1BDD,$0488,Sunduk))+' Darkness:'+IntToStr(CountEx($1BDD,$0485,Sunduk))+' Elven:'+IntToStr(CountEx($1BDD,$0498,Sunduk)));
end;

// Идем к сундуку и выгружаемся
procedure UnloadOrDead;
begin
  NewMoveXY(xTileSunduk, yTileSunduk, false, 0, true);
  if not Dead then begin Discharge; end
  else begin AddToSystemJournal('Персонаж мертв.'); SetARStatus(False); Disconnect; end;
end;

procedure ArmsLore;
var
d, t: TDateTime;

begin
  d:=StrToTime('0:00:11');
  if ((now - n) > d) or (n = 0) then
  begin
    t:=now;
    WaitTargetType($0F51);
    UseSkill('Arms Lore');
    WaitJournalLineSystem(t, 'This|tell', 3000);
    if TargetPresent then CancelTarget;
    n:=now;
  end;
end;

procedure TinkerHatchet;
begin
  UseObject(sunduk);
  if GetQuantity(FindType($1BF2, backpack)) > 0 then MoveItem(FindItem, GetQuantity(FindItem), Sunduk, 0, 0, 0);
  if GetQuantity(FindType($1BF2, Sunduk)) > 4 then
  begin
    repeat
      MoveItem(FindItem,4,backpack,0,0,0);
      Wait(500);
      if FindType($1EBC,backpack) = 0 then MoveItem(FindType($1EBC,Sunduk),1,backpack,0,0,0);
      WaitMenu('to make', 'Deadly Tools');
      WaitMenu('to make', 'Hatchet');
      UseType($1EBC,$ffff);
      WaitForTarget(5000);
      If TargetPresent then TargetToObject(FindType($1BF2,backpack));
      Wait(7300);
      MoveItem(FindType($1EBC,backpack),1,Sunduk,0,0,0);
    until FindType(Hatchet, backpack) > 0;
  end;
  if GetQuantity(FindType(Hatchet, backpack)) < 1 then 
  begin TinkerHatchet; end
  else begin Equip(RHandLayer, finditem); wait(500); end;
end;

// Рубим дерево (Edred)
function LumbCurTree(tile,x,y,z : Integer) : Boolean;
// рубим указанный тайл. Возвращаем false если перевес или чар мертв.
var
q, m1, m2, m3, m4, m5, m6, m7, m8, m9, CountFizzle, NextTree : integer;
t: TDateTime;
oldx, oldy : Integer;

begin
  Result := true;
  CountFizzle := 0;
  if (ObjAtLayer(LHandLayer) = 0) and (FindType(Hatchet, backpack) = 0)  then
  begin
    oldx := GetX(Self); oldy := GetY(Self);
    NewMoveXY(xTileSunduk,yTileSunduk,false,0,True);
    UOSay('banka');
    UseObject(sunduk);
    wait(1000);
    if FindType(Hatchet, Sunduk) > 0 then
    begin
      wait(500);
      Equip(RHandLayer, finditem);
      wait(500);
    end
    else
    begin
      TinkerHatchet;
      wait(500);
    end;
    NewMoveXY(oldx,oldy,false,0,True);
  end;
  wait(1000);
  repeat
    if UseArms = 1 then ArmsLore;
    t:=now;
    if WarMode = true then SetWarMode(false);
    if TargetPresent then CancelTarget;
    ctime := Now;
    UseType(Hatchet, $FFFF);
    WaitForTarget(5000);
    If TargetPresent then TargetToTile(tile, x, y, z);
    q := 0;
    repeat
      wait(100);
      q := q + 1;
      checksave;
      m1 := InJournalBetweenTimes(Msg1, ctime, Now);
      m2 := InJournalBetweenTimes(Msg2, ctime, Now);
      m3 := InJournalBetweenTimes(Msg3, ctime, Now);
      m4 := InJournalBetweenTimes(Msg4, ctime, Now);
      m5 := InJournalBetweenTimes(Msg5, ctime, Now);
      m6 := InJournalBetweenTimes(Msg6, ctime, Now);
      m7 := InJournalBetweenTimes(Msg7, ctime, Now);
      m8 := InJournalBetweenTimes(Msg8, ctime, Now);
      m9 := InJournalBetweenTimes(Msg9, ctime, Now);
    until (m1<>-1) or (m2<>-1) or (m3<>-1) or (m4<>-1) or (m5<>-1) or (m6<>-1) or (m7<>-1) or (m8<>-1) or (m9<>-1) or Dead or (q > 150);
    if (m2<>-1) or (m3<>-1) or (m4<>-1) then CountFizzle := CountFizzle + 1;
    if Dead or (Weight > MyMaxWeight) then begin Result := false;  end;
    if (q > 150) then NextTree := NextTree + 1;
  until (m5<>-1) OR (m6<>-1) OR (m7<>-1) OR (m8<>-1) OR (m9<>-1) OR (CountFizzle = 10) OR (NextTree > 3);
  if NextTree >= 3 then NextTree := 0;
end;


// Главная функция
Begin
  InitTTilesArray;
  InitCTilesArrayFirst;
  InitSystem;
  InitReg;
  MarkTrees;
  repeat
    for i:= 0 to Length(ChopTilesArray) - 1 do
    begin
      NewMoveXY(ChopTilesArray[i].x, ChopTilesArray[i].y, false, 1, false);
      if not LumbCurTree(ChopTilesArray[i].tile, ChopTilesArray[i].x, ChopTilesArray[i].y, ChopTilesArray[i].z) then UnloadOrDead;
    end;
  until Dead;

End.SetGlobal