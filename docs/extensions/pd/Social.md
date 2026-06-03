---
search:
  boost: 10.0
---

# Class: Social 


_Information about social aspects such as family, public life, or_

_professional networks_



<div data-search-exclude markdown="1">



URI: [pd:Social](https://w3id.org/lmodel/dpv/pd/Social)





```mermaid
 classDiagram
    class Social
    click Social href "../Social/"
      Social <|-- Communication
        click Communication href "../Communication/"
      Social <|-- Criminal
        click Criminal href "../Criminal/"
      Social <|-- Family
        click Family href "../Family/"
      Social <|-- Professional
        click Professional href "../Professional/"
      Social <|-- PublicLife
        click PublicLife href "../PublicLife/"
      Social <|-- SocialBehaviour
        click SocialBehaviour href "../SocialBehaviour/"
      Social <|-- SocialNetwork
        click SocialNetwork href "../SocialNetwork/"
      
      
```





## Inheritance
* **Social**
    * [Communication](Communication.md)
    * [Criminal](Criminal.md)
    * [Family](Family.md)
    * [Professional](Professional.md)
    * [PublicLife](PublicLife.md)
    * [SocialNetwork](SocialNetwork.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Social](https://w3id.org/lmodel/dpv/pd/Social) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Social |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Social |
| native | pd:Social |
| exact | dpv_pd:Social, dpv_pd_owl:Social |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Social
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Social
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about social aspects such as family, public life, or

  professional networks'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social
exact_mappings:
- dpv_pd:Social
- dpv_pd_owl:Social
class_uri: pd:Social

```
</details>

### Induced

<details>
```yaml
name: Social
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Social
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about social aspects such as family, public life, or

  professional networks'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social
exact_mappings:
- dpv_pd:Social
- dpv_pd_owl:Social
class_uri: pd:Social

```
</details></div>