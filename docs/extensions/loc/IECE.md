---
search:
  boost: 10.0
---

# Class: IECE 


_Concept representing region County Clare in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-CE](https://w3id.org/lmodel/dpv/loc/IE-CE)





```mermaid
 classDiagram
    class IECE
    click IECE href "../IECE/"
      IE <|-- IECE
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IECE**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-CE](https://w3id.org/lmodel/dpv/loc/IE-CE) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-CE
* County Clare




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-CE |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-CE |
| native | loc:IECE |
| exact | dpv_loc:IE-CE, dpv_loc_owl:IE-CE |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IECE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Clare in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CE
- County Clare
exact_mappings:
- dpv_loc:IE-CE
- dpv_loc_owl:IE-CE
is_a: IE
class_uri: loc:IE-CE

```
</details>

### Induced

<details>
```yaml
name: IECE
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-CE
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Clare in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-CE
- County Clare
exact_mappings:
- dpv_loc:IE-CE
- dpv_loc_owl:IE-CE
is_a: IE
class_uri: loc:IE-CE

```
</details></div>