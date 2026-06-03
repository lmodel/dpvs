---
search:
  boost: 10.0
---

# Class: IED 


_Concept representing region County Dublin in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-D](https://w3id.org/lmodel/dpv/loc/IE-D)





```mermaid
 classDiagram
    class IED
    click IED href "../IED/"
      IE <|-- IED
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IED**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-D](https://w3id.org/lmodel/dpv/loc/IE-D) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-D
* County Dublin




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-D |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-D |
| native | loc:IED |
| exact | dpv_loc:IE-D, dpv_loc_owl:IE-D |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IED
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Dublin in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-D
- County Dublin
exact_mappings:
- dpv_loc:IE-D
- dpv_loc_owl:IE-D
is_a: IE
class_uri: loc:IE-D

```
</details>

### Induced

<details>
```yaml
name: IED
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-D
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Dublin in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-D
- County Dublin
exact_mappings:
- dpv_loc:IE-D
- dpv_loc_owl:IE-D
is_a: IE
class_uri: loc:IE-D

```
</details></div>