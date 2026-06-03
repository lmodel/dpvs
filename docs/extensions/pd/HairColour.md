---
search:
  boost: 10.0
---

# Class: HairColour 


_Information about hair colour_



<div data-search-exclude markdown="1">



URI: [pd:HairColour](https://w3id.org/lmodel/dpv/pd/HairColour)





```mermaid
 classDiagram
    class HairColour
    click HairColour href "../HairColour/"
      PhysicalCharacteristic <|-- HairColour
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **HairColour**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HairColour](https://w3id.org/lmodel/dpv/pd/HairColour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Hair Colour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HairColour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HairColour |
| native | pd:HairColour |
| exact | dpv_pd:HairColour, dpv_pd_owl:HairColour |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HairColour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HairColour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about hair colour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Hair Colour
exact_mappings:
- dpv_pd:HairColour
- dpv_pd_owl:HairColour
is_a: PhysicalCharacteristic
class_uri: pd:HairColour

```
</details>

### Induced

<details>
```yaml
name: HairColour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HairColour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about hair colour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Hair Colour
exact_mappings:
- dpv_pd:HairColour
- dpv_pd_owl:HairColour
is_a: PhysicalCharacteristic
class_uri: pd:HairColour

```
</details></div>