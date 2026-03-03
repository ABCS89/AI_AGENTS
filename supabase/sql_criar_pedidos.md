create table public.pedidos (
    id uuid primary key default uuid_generate_v4(),
    empresa_id uuid references public.empresas(id) on delete cascade,
    cliente_nome varchar(150),
    cliente_telefone varchar(30),
    valor_total numeric(10,2),
    status varchar(50) default 'pendente',
    created_at timestamp with time zone default now()
);