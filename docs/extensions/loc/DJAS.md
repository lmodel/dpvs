---
search:
  boost: 10.0
---

# Class: DJAS 


_Concept representing region Ali Sabieh Region in country Djibouti_



<div data-search-exclude markdown="1">



URI: [loc:DJ-AS](https://w3id.org/lmodel/dpv/loc/DJ-AS)





```mermaid
 classDiagram
    class DJAS
    click DJAS href "../DJAS/"
      DJ <|-- DJAS
        click DJ href "../DJ/"
      
      
```





## Inheritance
* [DJ](DJ.md)
    * **DJAS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:DJ-AS](https://w3id.org/lmodel/dpv/loc/DJ-AS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* DJ-AS
* Ali Sabieh Region




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#DJ-AS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:DJ-AS |
| native | loc:DJAS |
| exact | dpv_loc:DJ-AS, dpv_loc_owl:DJ-AS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DJAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DJ-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ali Sabieh Region in country Djibouti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DJ-AS
- Ali Sabieh Region
exact_mappings:
- dpv_loc:DJ-AS
- dpv_loc_owl:DJ-AS
is_a: DJ
class_uri: loc:DJ-AS

```
</details>

### Induced

<details>
```yaml
name: DJAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#DJ-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Ali Sabieh Region in country Djibouti
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- DJ-AS
- Ali Sabieh Region
exact_mappings:
- dpv_loc:DJ-AS
- dpv_loc_owl:DJ-AS
is_a: DJ
class_uri: loc:DJ-AS

```
</details></div>