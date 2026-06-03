---
search:
  boost: 10.0
---

# Class: Demographic 


_Information about demography and demographic characteristics_



<div data-search-exclude markdown="1">



URI: [pd:Demographic](https://w3id.org/lmodel/dpv/pd/Demographic)





```mermaid
 classDiagram
    class Demographic
    click Demographic href "../Demographic/"
      External <|-- Demographic
        click External href "../External/"
      

      Demographic <|-- Geographic
        click Geographic href "../Geographic/"
      Demographic <|-- IncomeBracket
        click IncomeBracket href "../IncomeBracket/"
      Demographic <|-- PhysicalTrait
        click PhysicalTrait href "../PhysicalTrait/"
      

      
```





## Inheritance
* [External](External.md)
    * **Demographic**
        * [Geographic](Geographic.md)
        * [IncomeBracket](IncomeBracket.md)
        * [PhysicalTrait](PhysicalTrait.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Demographic](https://w3id.org/lmodel/dpv/pd/Demographic) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Demographic




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Demographic |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Demographic |
| native | pd:Demographic |
| exact | dpv_pd:Demographic, dpv_pd_owl:Demographic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Demographic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Demographic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about demography and demographic characteristics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Demographic
exact_mappings:
- dpv_pd:Demographic
- dpv_pd_owl:Demographic
is_a: External
class_uri: pd:Demographic

```
</details>

### Induced

<details>
```yaml
name: Demographic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Demographic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about demography and demographic characteristics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Demographic
exact_mappings:
- dpv_pd:Demographic
- dpv_pd_owl:Demographic
is_a: External
class_uri: pd:Demographic

```
</details></div>