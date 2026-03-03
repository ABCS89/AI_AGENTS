-- Ativar extensão para UUID (caso ainda não esteja ativa)
create extension if not exists "uuid-ossp";

-- Criar tabela produtos
create table public.produtos (
    id uuid primary key default uuid_generate_v4(),
    nome varchar(150) not null,
    categoria varchar(100) not null,
    preco numeric(10,2) not null check (preco >= 0),
    ativo boolean default true,
    created_at timestamp with time zone default now(),
    updated_at timestamp with time zone default now()
);

-- Criar tabela empresas
create table public.empresas (
    id uuid primary key default uuid_generate_v4(),
    nome varchar(150) not null,
    created_at timestamp with time zone default now()
);

-- Adicionar empresa_id em produtos
alter table public.produtos
add column empresa_id uuid references public.empresas(id) on delete cascade;


-- Criar index para busca por categoria
create index idx_produtos_categoria on public.produtos(categoria);

-- Trigger para atualizar updated_at automaticamente
create or replace function public.update_updated_at_column()
returns trigger as $$
begin
   new.updated_at = now();
   return new;
end;
$$ language plpgsql;

create trigger update_produtos_updated_at
before update on public.produtos
for each row
execute procedure public.update_updated_at_column();

-- Ativar Row Level Security
alter table public.produtos enable row level security;

-- Política liberando leitura pública (ajuste depois se quiser vender via API)
create policy "Permitir leitura publica"
on public.produtos
for select
using (true);

-- Inserindo os produtos base
insert into public.produtos (nome, categoria, preco, ativo)
values
('Arte A4', 'arte', 29.90, true),
('Arte A3', 'arte', 49.90, true),
('Arte Personalizada Premium', 'arte', 89.90, true),
('Logo Simples', 'design', 120.00, true);