---
search:
  boost: 10.0
---

# Class: Tattoo 


_Information about tattoos_



<div data-search-exclude markdown="1">



URI: [pd:Tattoo](https://w3id.org/lmodel/dpv/pd/Tattoo)





```mermaid
 classDiagram
    class Tattoo
    click Tattoo href "../Tattoo/"
      PhysicalCharacteristic <|-- Tattoo
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Tattoo**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Tattoo](https://w3id.org/lmodel/dpv/pd/Tattoo) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Tattoo




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Tattoo |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Tattoo |
| native | pd:Tattoo |
| exact | dpv_pd:Tattoo, dpv_pd_owl:Tattoo |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Tattoo
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tattoo
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about tattoos
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tattoo
exact_mappings:
- dpv_pd:Tattoo
- dpv_pd_owl:Tattoo
is_a: PhysicalCharacteristic
class_uri: pd:Tattoo

```
</details>

### Induced

<details>
```yaml
name: Tattoo
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Tattoo
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about tattoos
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Tattoo
exact_mappings:
- dpv_pd:Tattoo
- dpv_pd_owl:Tattoo
is_a: PhysicalCharacteristic
class_uri: pd:Tattoo

```
</details></div>