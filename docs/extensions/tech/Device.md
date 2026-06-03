---
search:
  boost: 10.0
---

# Class: Device 


_Device or computing device_



<div data-search-exclude markdown="1">



URI: [tech:Device](https://w3id.org/lmodel/dpv/tech/Device)





```mermaid
 classDiagram
    class Device
    click Device href "../Device/"
      Hardware <|-- Device
        click Hardware href "../Hardware/"
      

      Device <|-- IoTDevice
        click IoTDevice href "../IoTDevice/"
      Device <|-- PersonalComputer
        click PersonalComputer href "../PersonalComputer/"
      Device <|-- Telephone
        click Telephone href "../Telephone/"
      

      
```





## Inheritance
* **Device** [ [Hardware](Hardware.md)]
    * [Telephone](Telephone.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Device](https://w3id.org/lmodel/dpv/tech/Device) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Device




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Device |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Device |
| native | tech:Device |
| exact | dpv_tech:Device, dpv_tech_owl:Device |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Device
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Device
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Device or computing device
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Device
exact_mappings:
- dpv_tech:Device
- dpv_tech_owl:Device
mixins:
- Hardware
class_uri: tech:Device

```
</details>

### Induced

<details>
```yaml
name: Device
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Device
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Device or computing device
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Device
exact_mappings:
- dpv_tech:Device
- dpv_tech_owl:Device
mixins:
- Hardware
class_uri: tech:Device

```
</details></div>