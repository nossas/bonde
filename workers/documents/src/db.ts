import { Sequelize, Model, DataTypes } from 'sequelize';

const sequelize = new Sequelize(process.env.DATABASE_URL || 'sqlite::memory:')

export const getActions = async(communityId:number, kind:string, modelAction:any, models: any) => {
    return await models.Community.findAndCountAll({
      include: {
        model: models.Mobilization,
        include: [{
          model: models.Block,
          include: [{
            model: models.Widget,
            where: {
              kind: kind
            },
            include: [{
                model: modelAction,
            }]
          }]
        }]
      },
      where: {
        id: communityId
      }
    });
}

export const check = async () => {
    try {
        await sequelize.authenticate();
        console.log('Connection has been established successfully.');
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
};

export const model = () => {

    class Community extends Model { }
    class Mobilization extends Model { }
    class Block extends Model { }
    class Widget extends Model { }
    class FormEntry extends Model { }
    class PressureByEmail extends Model { }
    class PressureByPhone extends Model { }
    class Donation extends Model { }
    class Activist extends Model { }

    Community.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        name: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'community' });

    Mobilization.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        name: DataTypes.STRING,
        slug: DataTypes.STRING,
        customDomain: DataTypes.STRING,
        communityId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE,
        deletedAt: 'deleted_at'
    }, { underscored: true, sequelize, modelName: 'mobilization' });

    Community.hasMany(Mobilization);
    Mobilization.belongsTo(Community);

    Block.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        mobilizationId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'block' });

    Mobilization.hasMany(Block);
    Block.belongsTo(Mobilization);

    Widget.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        blockId: DataTypes.STRING,
        kind: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'widget' });

    Block.hasMany(Widget);
    Widget.belongsTo(Block);

    FormEntry.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        widgetId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        fields: DataTypes.HSTORE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'form_entry' });

    Widget.hasMany(FormEntry);
    FormEntry.belongsTo(Widget);

    PressureByEmail.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        widgetId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'activist_pressure' });

    Widget.hasMany(PressureByEmail);
    PressureByEmail.belongsTo(Widget);

    PressureByPhone.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        widgetId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'twilio_call' });

    Widget.hasMany(PressureByPhone);
    PressureByPhone.belongsTo(Widget);

    Donation.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        widgetId: DataTypes.STRING,
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'donation' });

    Widget.hasMany(Donation);
    Donation.belongsTo(Widget);

    Activist.init({
        id: { type: DataTypes.STRING, primaryKey: true },
        createdAt: DataTypes.DATE,
        updatedAt: DataTypes.DATE
    }, { underscored: true, sequelize, modelName: 'activist' });

    return {
        Community,
        Mobilization,
        Block,
        Widget,
        FormEntry,
        PressureByEmail,
        PressureByPhone,
        Donation,
        Activist
    };
};