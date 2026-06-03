---
search:
  boost: 10.0
---

# Class: IEG 


_Concept representing region County Galway in country Ireland_



<div data-search-exclude markdown="1">



URI: [loc:IE-G](https://w3id.org/lmodel/dpv/loc/IE-G)





```mermaid
 classDiagram
    class IEG
    click IEG href "../IEG/"
      IE <|-- IEG
        click IE href "../IE/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [IE](IE.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **IEG**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IE-G](https://w3id.org/lmodel/dpv/loc/IE-G) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IE-G
* County Galway




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IE-G |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IE-G |
| native | loc:IEG |
| exact | dpv_loc:IE-G, dpv_loc_owl:IE-G |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IEG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-G
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Galway in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-G
- County Galway
exact_mappings:
- dpv_loc:IE-G
- dpv_loc_owl:IE-G
is_a: IE
class_uri: loc:IE-G

```
</details>

### Induced

<details>
```yaml
name: IEG
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IE-G
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region County Galway in country Ireland
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IE-G
- County Galway
exact_mappings:
- dpv_loc:IE-G
- dpv_loc_owl:IE-G
is_a: IE
class_uri: loc:IE-G

```
</details></div>